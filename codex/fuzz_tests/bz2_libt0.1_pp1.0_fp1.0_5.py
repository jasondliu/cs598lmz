import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# 压缩文件
with bz2.BZ2File('spam.bz2', 'wb') as f:
    f.write(b'Hello World!')

with bz2.BZ2File('spam.bz2', 'rb') as f:
    print(f.read())

# 压缩文件
data = open('spam.bz2', 'rb').read()
print(len(data))

data2 = bz2.compress(b'Hello World!')
print(len(data2))

print(bz2.decompress(data2))

# 压缩文件
import bz2
uncompressed = b'We are the knights who say Ni!'
compressed = bz2.compress(uncompressed)
print(compressed)

print(bz2.decompress(compressed))

# 压缩文
