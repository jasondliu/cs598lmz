from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
And here's a way to decompress a whole file:
from lzma import open
with open('hello.xz') as f:
    file_content = f.read()
'''

#
# 用于解压缩字符串
#
def ungzip(data):
    try:
        # print '正在解压.....'
        data = gzip.decompress(data)
        # print '解压完毕!'
    except:
        print('未经压缩, 无需解压')
    return data

#
# 用于解压缩字符串
#
def unxz(data):
    try:
        # print '正在解压.....'
        #data = lzma.decompress(data)
        data = LZMADecompressor().decompress
