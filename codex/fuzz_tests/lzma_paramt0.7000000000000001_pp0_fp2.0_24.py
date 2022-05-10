from lzma import LZMADecompressor
LZMADecompressor()

# compress and decompress
data = b'Lots of data here'
compressor = LZMADecompressor()
compressor.decompress(data)
compressor.unused_data

# decompress a series of chunks
compressor = LZMADecompressor()
chunk = compressor.decompress(data[:100])
chunk = compressor.decompress(data[100:])

# decompress a file-like object
with open('lorem.xz', 'rb') as input:
    with LZMADecompressor() as decompressor:
        for block in iter(lambda: input.read(64 * 1024), b''):
            output.write(decompressor.decompress(block))
    output.write(decompressor.flush())

# decompress a file
with open('lorem.xz', 'rb') as input, open('lorem', 'wb') as output:
    with LZMADecompressor() as decompressor:
        output.write(decompressor.decompress(input.read()))
