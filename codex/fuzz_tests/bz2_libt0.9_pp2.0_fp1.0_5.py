import bz2
bz2.compress(b'aaaaaaaa'*100)

# 可以读取到文件当中的普通文件，但是不能读取压缩文件，可以用来检查结果是否正常
# ···
# with bz2.open('file.bz2', 'rt') as f:
#     data = f.read()
# # ···

#可以压缩文件
# data = bz2.compress(b'aaaaaaaa')
# with open('file.bz2', 'wb') as f:
#     f.write(data)

#可以解压文件
# compressed = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\
