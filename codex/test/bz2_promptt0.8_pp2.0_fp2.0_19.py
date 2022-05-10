import bz2
# Test BZ2Decompressor ()

bz_comp = bz2.BZ2Compressor()
bz_decomp = bz2.BZ2Decompressor()

s = '<xml>BZ</xml>'.encode('utf-8')

# 压缩
comp = bz_comp.compress(s)
print('comp:', len(comp))
print('txt:', comp)

# 解压
decomp = bz_decomp.decompress(comp)
print('decomp:', decomp)

# 关闭
