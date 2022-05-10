import lzma
# Test LZMADecompressor
# if __name__ == '__main__':
#     print('Test LZMADecompressor')
#     decomp = lzma.LZMADecompressor()
#     with open('data/enwik9.xz', 'rb') as f:
#         data = f.read()
#     txt = decomp.decompress(data)
#     print(txt.decode("utf-8")[:100])
#     print(len(txt))
# Test LZMADecompressor
if __name__ == '__main__':
    print('Test LZMADecompressor')
    decomp = lzma.LZMADecompressor()
