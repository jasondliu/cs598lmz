import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#example
inp = open("test.xz", "rb")
decompressor = lzma.LZMADecompressor()
next_data = inp.read(100)
while next_data:
    data = decompressor.decompress(next_data)
    if data:
        print(data)
    next_data = inp.read(100)
inp.close()

# Use LZMAFile
# https://docs.python.org/3/library/lzma.html#using-lzmafile
inp = open("test.xz", "rb")
f = lzma.LZMAFile(inp)
file_content = f.read()
f.close()
inp.close()
print(file_content)

# Use open, read, close
# https://docs.python.org/3/library/lzma.html#opening-files
f = lzma.open("test.xz")
file_content
