import json
import codecs

s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
	s = ''
	for c in input_str:
		if c in s1:
			s += s0[s1.index(c)]
		else:
			s += c
	return s

class Output:
	result = {
			'id':		'',
			'agency':	'',     # có qua môi giới hay không ? Yes/No/Not sure
	}


with open('data_10000.json','rb') as json_data:
    data_set = json.loads(json_data.read())
    print(len(data_set), "datas loaded succesfully")

    MG_keyword = 'MT TL LH STST MTG pháp lý HĐT hỗ trợ vay hợp đồng thuê'  # từ khóa nhận diện môi giới
    CC_keyword = 'chính chủ miễn trung gian cò'                            # từ khóa nhận diện chính chủ
    bagOfWordsMG = MG_keyword.split(' ')                                   # túi từ môi giới
    bagOfWordsCC = CC_keyword.split(' ')                                   # túi từ chính chủ
    for data in data_set:
        output = Output()
        output.result['id'] = data['id']
        bagOfWordsText = data['content'].split(' ')                        # túi từ nội dung
        uniqueWords_CC = set(bagOfWordsCC).union(set(bagOfWordsText))
        numOfWords_CC = dict.fromkeys(uniqueWords_CC, 0)

        check_MG = 0  # if check_MG = 0, agency = 'No'
        check_CC = 0  # if check_CC = 0, agency = 'Yes'
        # if (MG,CC) = (0, !=0) <=> agency = 'No' (nhà chính chủ)
        # if (MG,CC) = (!=0, 0) <=> agency = 'Yes' (nhà môi giới)
        # else agency = 'Not sure'

        ## kiểm tra icon trong văn bản
        Text_removed_accents = remove_accents(data['content'])
        check_icon = 0
        for letter in Text_removed_accents:
            ascii_key = ord(letter)
            if (ascii_key > 126 or (ascii_key < 32 and ascii_key != 10 and ascii_key != 13)):
                # có icon <=> nhà môi giới (gán check_MG = 1), chỉ kiểm tra thêm túi từ chính chủ
                check_icon += 1
                check_MG = 1
                for word in bagOfWordsText:
                    numOfWords_CC[word] += 1
                for word in bagOfWordsCC:
                    check_CC += numOfWords_CC[word]
                break
        if (check_icon == 0):
            #không có icon, kiểm tra cả túi từ môi giới và chính chủ
            uniqueWords_MG = set(bagOfWordsMG).union(set(bagOfWordsText))
            numOfWords_MG = dict.fromkeys(uniqueWords_MG, 0)
            for word in bagOfWordsText:
                numOfWords_MG[word] += 1
                numOfWords_CC[word] += 1
            for word in bagOfWordsMG:
                check_MG += numOfWords_MG[word]
            for word in bagOfWordsCC:
                check_CC += numOfWords_CC[word]

        # phân loại nhà chính chủ
        if (check_MG == 0 and check_CC != 0):
            output.result['agency'] = 'No'
        elif (check_MG != 0 and check_CC == 0):
            output.result['agency'] = 'Yes'
        else:
            output.result['agency'] = 'Not sure'

        # ghi file
        with codecs.open('result_1.json', 'a') as reader:
            json.dump(output.result, reader)
        #print('Ghi file thanh cong !')
        #break;
