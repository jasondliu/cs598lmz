import bz2
bz2_file=bz2.BZ2File('test.txt.bz2','rb')
print(bz2_file.read())

# 压缩
bz2_file_compressed=bz2.BZ2File('test_compressed.txt.bz2','wb')
bz2_file_compressed.write(data)
bz2_file_compressed.close()

# 压缩后的文件都是经过小端模式编码，使用Python的struct模块可以解码
import struct
f=open(b'example.bz2','rb')
data=f.read(4)
print(data)
print(struct.unpack('i',data))
