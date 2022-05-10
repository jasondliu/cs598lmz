import lzma
lzma.LZMACompressor()

section = iconv('silesia.tar')
comp = bz2.BZ2Compressor(9)

f = open('silesia.tar.xz', 'wb')
f.write(comp.compress(section))
f.close()
