from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

with open('data.txt', 'rb') as f:
    decompressor = LZMADecompressor()
    data = decompressor.decompress(f.read())
with open('data.txt', 'rb') as f:
    decompressor = LZMADecompressor()
    for chunk in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(chunk)
        process(data)
    data = decompressor.flush()
    process(data)

compressed_data = b'x\x9cK\xcb\xcf\x07\r\xc9\x14\x80\x02\x02\x1d\t\xc9\xa8@\x04\x00\x85\xa6?7\x05\x89 \x04\xa6\xa3d\x1b,\xcdI\xee\x02\x00!\x01\x16\x00?\xc4\x00\x
