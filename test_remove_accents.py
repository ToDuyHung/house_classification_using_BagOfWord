sentence = "Đất nền nhà phố full thổ cư\nSổ sẵn riêng từng nền\n\nCó công viên nội khu - hồ tiểu cảnh\nHạ tầng đạt chuẩn - cống - đường - điện - nước\n\n(Đường rộng rãi) \n\rCạnh khu qui hoạch qui mô lớn chuyên nghỉ dưỡng và gần nhiều điểm du lịch nổi tiếng.....\n\rKhông khí mát mẻ - trong lành - cụm dân cư phát triển mạnh \n\rHiện đang nhận giữ chỗ thiện chí có hoàn trả 100% cho giai đoạn 1\n\rKhách hàng giữ chỗ sẽ được ưu tiên chọn lô và xem đất trước ngày mở bán ... và còn nhiều ưu đãi khác \n\rLiên hệ : 0788546059 Nhiên"
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
new_sentence = remove_accents(sentence)
check = 0
for word in new_sentence:
    ascii_key = ord(word)
    if (ascii_key > 126 or (ascii_key < 32 and ascii_key != 10 and ascii_key != 13)):
        check += 1
        print('có icon')
        print(word)
        break
if (check == 0):
    print('không có icon')

