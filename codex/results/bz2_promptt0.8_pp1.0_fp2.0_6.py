import bz2
# Test BZ2Decompressor
c = bz2.BZ2Compressor()
d = c.compress(b'9')
d += c.compress(b'8')
d += c.compress(b'7')
d += c.flush()
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(d)

decompressor.decompress(b'6')
decompressor.flush()

# Test BZ2File

# with open('example.txt', 'rb') as f:
#     original_data = f.read()
# with bz2.BZ2File('example.txt.bz2', 'wb') as f:
#     f.write(original_data)
#
# with bz2.BZ2File('example.txt.bz2', 'rb') as f:
#     assert f.read() == original_data
#
# with bz2.BZ2File('example.txt.bz2', 'r') as f:
#     assert f.read() == original_data
