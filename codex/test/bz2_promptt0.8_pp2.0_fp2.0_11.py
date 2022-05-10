import bz2
# Test BZ2Decompressor

source = [b'x' * 100, b'x' * 100]
comp = bz2.BZ2Compressor()
cdata = b''
for seq in source:
    cdata += comp.compress(seq)
cdata += comp.flush()

print(cdata)

decompresser = bz2.BZ2Decompressor()
dres = []
