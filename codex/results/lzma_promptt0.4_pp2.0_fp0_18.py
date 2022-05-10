import lzma
# Test LZMADecompressor()

lzc = lzma.LZMADecompressor()

with open('data/enwik8.lzma', 'rb') as f_in, open('data/enwik8.txt', 'wb') as f_out:
    f_out.write(lzc.decompress(f_in.read()))

# Test LZMADecompressor.decompress()

with open('data/enwik8.lzma', 'rb') as f_in, open('data/enwik8.txt', 'wb') as f_out:
    f_out.write(lzma.decompress(f_in.read()))

# Test LZMADecompressor.decompress() with chunks

with open('data/enwik8.lzma', 'rb') as f_in, open('data/enwik8.txt', 'wb') as f_out:
    lzc = lzma.LZMADecompressor()
    for chunk in iter(lambda: f_in.read(1024
