import lzma
# Test LZMADecompressor
with lzma.open("test.xz", "rb") as f:
    file_content = f.read()
    print(file_content)

# Test LZMACompressor
with lzma.open("test.xz", "wb") as f:
    f.write(b"Hello")

# Test LZMAFile
with open("test.xz", "rb") as f:
    with lzma.LZMAFile(f) as lz:
        print(lz.read())

with open("test.xz", "wb") as f:
    with lzma.LZMAFile(f, mode="w") as lz:
        lz.write(b"Hello")

# Test LZMAError
