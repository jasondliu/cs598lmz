import lzma
# Test LZMADecompressor
with lzma.LZMADecompressor() as dec:
    with open('tmp/example.xz', 'rb') as f:
        file_content = f.read()
        data = dec.decompress(file_content)
        print(data)

# Test LZMAFile
with lzma.open('tmp/example.xz') as f:
    file_content = f.read()
    print(file_content)
