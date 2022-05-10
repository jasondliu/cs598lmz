import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(bz2.decompress(data))
print(bz2.decompress(data).decode('utf-8'))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print(decompressor.decompress(data).decode('utf-8'))

decompressor = bz2.BZ2Decompressor()
for chunk in iter(lambda: file.read(100 * 1024), b''):
    decompressor.decompress(chunk)

uncompressed_data = decompressor.flush()

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
for data
