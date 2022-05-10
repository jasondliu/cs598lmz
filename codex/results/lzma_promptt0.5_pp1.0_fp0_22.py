import lzma
# Test LZMADecompressor
data = b'x\x9c+\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00 \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

with lzma.LZMADecompressor() as dec:
    print(dec.decompress(data))

with lzma.open('example.xz', 'rt') as f:
    text = f.read()
    print(text)

with lzma.open('example.xz', 'rt', encoding='utf-8') as f:
    text = f.read()
    print(text)

with lzma.open('example.xz', 'rt', encoding='utf-8', errors='ignore') as f:
    text = f.read()
    print(text)


# Test LZMAFile
with lzma.open('example.xz', 'rb') as f:
    file_content = f
