from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

'''

Base64
Base64 是一种用64个字符来表示任意二进制数据的方法。

Base64 编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不是3的倍数，最后会剩下1个或2
