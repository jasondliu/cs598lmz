from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)
# b'foobar'

with open('compressed-data', 'rb') as input, open('uncompressed-data', 'wb') as output:
    decompressor = LZMADecompressor()
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))
    output.write(decompressor.flush())
</code>

