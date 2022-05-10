import bz2
bz2.decompress(bz2_data)

# 使用bz2.BZ2Compressor和bz2.BZ2Decompressor类创建压缩器和解压程序对象
comp = bz2.BZ2Compressor()
comp.compress(b'hello world!')
comp.flush()

decomp = bz2.BZ2Decompressor()
decomp.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
decomp.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
