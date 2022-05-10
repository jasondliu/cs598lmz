import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
with open('enwik9', 'rb') as in_file, open('enwik9.uncompressed', 'wb') as out_file:
    for buf in iter(partial(in_file.read, 1024*1024), b''):
        out_file.write(decompressor.decompress(buf))
    out_file.write(decompressor.flush())
# Test LZMACompressor
compressor = lzma.LZMACompressor()
with open('enwik9.uncompressed', 'rb') as in_file, open('enwik9.compressed', 'wb') as out_file:
    for buf in iter(partial(in_file.read, 1024*1024), b''):
        out_file.write(compressor.compress(buf))
    out_file.write(compressor.flush())
# Test LZMAFile
with lzma.open('enwik9.compressed.lzma', 'rb') as f:
    data = f.read()

