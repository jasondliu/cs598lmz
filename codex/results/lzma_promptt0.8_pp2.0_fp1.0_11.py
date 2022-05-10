import lzma
# Test LZMADecompressor

with lzma.open('out.xz', 'rb') as raw:
    with lzma.open('in.txt', 'wb') as raw2:
        raw2.write(raw.read())
# Test LZMACompressor

with lzma.open('out.xz', 'wb') as raw:
    with lzma.open('in.txt', 'rb') as raw2:
        raw.write(raw2.read())
 
# Test LZMADecompressor

decomp = lzma.LZMADecompressor()
compressed = open('out.xz', 'rb').read()
decompressed = decomp.decompress(compressed)
open('in.txt', 'wb').write(decompressed)

# Test LZMACompressor

comp = lzma.LZMACompressor()
uncompressed = open('in.txt', 'rb').read()
compressed = comp.compress(uncompressed)
compressed += comp.flush()
open('out.xz', 'wb').
