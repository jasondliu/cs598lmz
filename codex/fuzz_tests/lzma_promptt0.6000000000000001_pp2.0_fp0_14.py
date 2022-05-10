import lzma
# Test LZMADecompressor.decompress()
comp = lzma.LZMADecompressor()
with open('lzma/test1.xz', 'rb') as infile, open('lzma/test1.out', 'wb') as outfile:
    while True:
        chunk = infile.read(10240)
        if len(chunk) == 0:
            break
        outfile.write(comp.decompress(chunk))
    outfile.write(comp.flush())
# Test LZMADecompressor.decompress() using a file-like object
with open('lzma/test1.xz', 'rb') as infile, open('lzma/test1.out', 'wb') as outfile:
    decomp = lzma.LZMADecompressor()
    for chunk in iter(lambda: infile.read(10240), b''):
        outfile.write(decomp.decompress(chunk))
    outfile.write(decomp.flush())
# Test LZMADecompressor.decompress
