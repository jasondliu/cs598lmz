import lzma
# Test LZMADecompressor
# decomp = lzma.LZMADecompressor()
# print(decomp.decompress(data))

# Test LZMACompressor
# comp = lzma.LZMACompressor()
# out = b''
# out += comp.compress(b"This is ")
# out += comp.compress(b"a test")
# out += comp.flush()
# print(out)

# Test LZMAFile
# with open('test.txt', 'rb') as fp:
#     with lzma.open('test.txt.xz', 'wt') as cf:
#         cf.write('This is a test')
#         cf.write(fp.read())

# with lzma.open('test.txt.xz', 'rt') as cf:
#     print(cf.read())

# Test LZMADecompressor
# with open('test.txt.xz', 'rb') as fp:
#     with lzma.open('test.txt', 'wt') as cf:
#        
