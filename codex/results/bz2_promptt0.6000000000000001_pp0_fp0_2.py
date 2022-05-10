import bz2
# Test BZ2Decompressor
with open("example.xml.bz2", 'rb') as f:
    d = bz2.BZ2Decompressor()
    text = d.decompress(f.read())
    print(text)

# Test BZ2File
with bz2.BZ2File("example.xml.bz2", 'rb') as f:
    text = f.read()
    print(text)

# Test BZ2Compressor
with open("example.xml.bz2", 'rb') as f:
    d = bz2.BZ2Compressor()
    text = d.compress(f.read())
    print(text)

# Test BZ2File
with bz2.BZ2File("example.xml.bz2", 'wb') as f:
    text = f.write(b'Hello World')
    print(text)
