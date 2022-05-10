import lzma
# Test LZMADecompressor
#d = lzma.LZMADecompressor()
#with open("my_file.xz", "rb") as f:
#    file_content = f.read()
#    data = d.decompress(file_content)
#    print(data)

# Test LZMACompressor
#c = lzma.LZMACompressor()
#with open("test.xz", "wb") as f:
#    f.write(c.compress(b"Hello world!"))
#    f.write(c.flush())

# Test open
#with lzma.open("test.xz", "w") as f:
#    f.write(b"Hello world!")

# Test open
#with lzma.open("test.xz") as f:
#    file_content = f.read()
#    print(file_content)

# Test LZMAFile
#with lzma.open("test.xz") as input:
#    with open("test.txt", "wb") as output:
