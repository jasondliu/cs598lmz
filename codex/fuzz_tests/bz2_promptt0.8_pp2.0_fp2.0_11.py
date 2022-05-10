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
while cdata:
    data = decompresser.decompress(cdata)
    cdata = decompresser.unconsumed_tail
    dres.append(data)

print(b''.join(dres))

# Test BZ2File

source = [b'x' * 100, b'x' * 100]
comp = bz2.BZ2Compressor()
cdata = b''
for seq in source:
    cdata += comp.compress(seq)
cdata += comp.flush()

decompresser = bz2.BZ2Decompressor()
f = io.BytesIO(cdata)
decomp = bz2
