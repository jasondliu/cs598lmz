import bz2
# Test BZ2Decompressor
# decomp = bz2.BZ2Decompressor()
#
# fin = open('sample.bz2', 'rb')
# fout = open('sample.txt', 'wb')
#
# decomp.decompress(fin.read(100000))
# fout.write(decomp.unconsumed_tail)
# fin.close()
# fout.close()

# Test BZ2Compressor
comp = bz2.BZ2Compressor()

fin = open('sample.txt', 'rb')
fout = open('sample.bz2', 'wb')

fout.write(comp.compress(fin.read(100000)))
fout.write(comp.flush())
fin.close()
fout.close()
