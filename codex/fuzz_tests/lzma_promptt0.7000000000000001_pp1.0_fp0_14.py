import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
data = decompressor.decompress(b"x\x9c+&\xcf.\x01\x01\x80\x02\xff\xff")
data += decompressor.flush()
print(data)
# b'hello'

# Test LZMAFile
with lzma.open('/tmp/foo.xz', mode='wt') as f:
    f.write('hello')
with lzma.open('/tmp/foo.xz', mode='rt') as f:
    print(f.read())
# hello
