import lzma
# Test LZMADecompressor

lzc = lzma.LZMADecompressor()

with open('../data/enwik8', 'rb') as f:
    with open('../data/enwik8.decomp', 'wb') as fout:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            fout.write(lzc.decompress(chunk))
        fout.write(lzc.flush())
 
# Test LZMACompressor

lzc = lzma.LZMACompressor()

with open('../data/enwik8', 'rb') as f:
    with open('../data/enwik8.comp', 'wb') as fout:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            fout.write(lzc.compress(chunk))
        fout.write(lzc.flush())
 
# Test open

with lzma.open('../data/enwik8', 'rb') as f:
    with open
