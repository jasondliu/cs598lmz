import bz2
# Test BZ2Decompressor.multi_decompressor()
data = bz2.compress(b'\0' * 12000)

bzd = bz2.BZ2Decompressor()

decompressed = bzd.multi_decompress(data)# consumes all data
if decompressed != b'\0' * 12000:
    print('BZ2Decompressor.multi_decompressor() failed')

# Test BZ2Decompressor.__next__()
decompressed = bzd.multi_decompress(data)
try:
    while True:
        bzd.__next__()  # decompress one byte at a time
except EOFError:
    pass

if bzd.unused_data:
    print('BZ2Decompressor.__next__() failed')

# Test BZ2Decompressor.decompress()
decompressed = b''
compressed = bz2.compress(b'\0'*12000)
while compressed:
    chunk, compressed = compressed[:10], compressed[10:]
