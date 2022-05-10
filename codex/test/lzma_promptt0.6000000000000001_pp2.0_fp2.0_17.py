import lzma
# Test LZMADecompressor
# lz = lzma.LZMADecompressor()
# result = lz.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
# print(result)

# Test LZMA File
# with open('test.xz', 'rb') as f:
#     file_content = f.read()
# lz = lzma.LZMADecompressor()
# result = lz.decompress(file_content)
# print(result)

def xz_decompress(file):
    with open(file, 'rb') as f:
        file_content = f.read()
    lz = lzma.LZMADecompressor()
    result = lz.decompress(file_content)
    return result

