import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
with open('/home/kazushi/Downloads/test.xz', 'rb') as f:
    file_content = f.read()
    data = d.decompress(file_content)
    print(data)

# Test LZMAFile
with lzma.open('/home/kazushi/Downloads/test.xz') as f:
    file_content = f.read()
    print(file_content)
