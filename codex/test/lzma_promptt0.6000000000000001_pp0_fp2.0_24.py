import lzma
# Test LZMADecompressor
# src='/Users/matt/Desktop/test.lzma'
# dst='/Users/matt/Desktop/test.out'
# with lzma.open(src) as s, open(dst, 'wb') as d:
#     d.write(s.read())

# Test LZMACompressor
# src='/Users/matt/Desktop/test.in'
# dst='/Users/matt/Desktop/test.out'
# with lzma.open(dst, mode='wb') as d, open(src, 'rb') as s:
#     d.write(s.read())

# Test LZMADecompressor.decompress
# src='/Users/matt/Desktop/test.lzma'
# dst='/Users/matt/Desktop/test.out'
# with open(src, 'rb') as s, open(dst, 'wb') as d:
#     decompressor=lzma.LZMADecompressor()
#     while True:
#         buf=s.read
