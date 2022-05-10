import bz2
# Test BZ2Decompressor.decompress
print('%10s  %10s  %10s' % ('len(data)', 'blocksize', 'comp. ratio'))
print(78 * '-')
for blocksize in [1, 2, 3, 5, 10, 16, 60, 128, 512, 1024, 2048, 4096]:
    compressor = bz2.BZ2Compressor(blocksize=blocksize)
    data = b'dummy'
    compressed = b''
    while data:
        data = source.read(1024)
        compressed += compressor.compress(data)
    compressed += compressor.flush()
    decompressor = bz2.BZ2Decompressor()
    print('%10d  %10d  %10.1f' % (len(compressed), blocksize,
        len(source.read()) / float(len(compressed))))
    while compressed:
        chunk = compressed[:1024]
        compressed = compressed[1024:]
        decompressed = decompressor.decompress(chunk)
# Test BZ2Decompressor.decompress(max_length
