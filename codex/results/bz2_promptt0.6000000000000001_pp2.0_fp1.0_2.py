import bz2
# Test BZ2Decompressor
# This is not the right way to do it, but it works
# with bz2file.BZ2File('00.bz2', 'r') as f:
#     print(f.read())

# with open('00.bz2', 'rb') as f:
#     decompressor = bz2.BZ2Decompressor()
#     data = f.read(100)
#     while data:
#         print(decompressor.decompress(data))
#         data = f.read(100)

# This is the right way to do it
with bz2.BZ2File('00.bz2', 'rb') as f:
    print(f.read())

# Test BZ2Compressor
with bz2.BZ2File('11.bz2', 'wb') as f:
    f.write(b'Hello, World!')

with open('11.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    data = f.read(100
