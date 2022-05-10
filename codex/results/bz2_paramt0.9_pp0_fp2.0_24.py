from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

#解压缩成一个大的字节字符串
BZ2Decompressor().decompress(bz2_data).decode('utf-8')

#解压缩后不断迭代产生小块字符串
bz2_dec = BZ2Decompressor()
next(bz2_dec.decompress(bz2_data))

#进行压缩处理，查看状态
bz2_dec.decompress(b'X'*10)
bz2_dec.decompress(b'X'*10)
bz2_dec.decompress(b'X'*10)
bz2_dec.decompress(b'X'*10)
bz2_dec.decompress(b'Y')
bz2_dec.
