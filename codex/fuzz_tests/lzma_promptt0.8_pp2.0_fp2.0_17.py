import lzma
# Test LZMADecompressor
stream = lzma.LZMADecompressor()
with open('/home/vince/Documents/Compress/1MB.bin.xz', 'rb') as f:
    stream.decompress(f.read())

# Test BZ2Decompressor
stream = bz2.BZ2Decompressor()
with open('/home/vince/Documents/Compress/1MB.bin.bz2', 'rb') as f:
    stream.decompress(f.read())

# Test ZlibDecompressor
stream = zlib.decompressobj()
with open('/home/vince/Documents/Compress/1MB.bin.gz', 'rb') as f:
    stream.decompress(f.read())

# Test GzipFile
f = gzip.GzipFile('/home/vince/Documents/Compress/1MB.bin.gz')
f.read()
f.close()
