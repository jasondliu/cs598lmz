import bz2
bz2.BZ2Decompressor.flush()

def read_bz2_file(f):
	global file_num
	global flag
	global count
	print('file_num:{}, flag:{}, count:{}'.format(file_num, flag, count))
	num = 0
	buff = str()
	decompressor = bz2.BZ2Decompressor()
	f_out = open('E:/Data/Source/wiki/output/{}.txt'.format(file_num), 'wb')
	f = bz2.BZ2File(f, 'rb')
	for line in f:
		buff = buff + line.decode()
		num = num + 1
		if num % 1000 == 0:
			print('num:{}'.format(num), end='\r')
			count = count + 1
			if count % 2000 == 0:
				data = decompressor.decompress(buff.encode())
				f_out.write(data)
				f_
