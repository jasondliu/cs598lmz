import lzma
# Test LZMADecompressor
dec = lzma.LZMADecompressor()
with open('enwik8', 'rb') as f:
    for block in iter(lambda: f.read(64*1024), b''):
        data = dec.decompress(block)
        if data:
            print(data)
            break

# Test LZMACompressor
comp = lzma.LZMACompressor()
with open('enwik8', 'rb') as f:
    with open('enwik8.xz', 'wb') as f2:
        for block in iter(lambda: f.read(64*1024), b''):
            f2.write(comp.compress(block))
        f2.write(comp.flush())

# Test LZMAFile
with lzma.open('enwik8.xz', 'rb') as f:
    data = f.read(1024)
    print(data)

# Test LZMAFile with mode 'with'
with lzma.open('enwik8.xz', 'rb') as f:
   
