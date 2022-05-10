import lzma
lzma.open

def compress_file(src, dst):
    data = open(src, 'rb').read()
    compressed_data = zlib.compress(data)
    open(dst, 'wb').write(compressed_data)

def uncompress_file(src, dst):
    data = open(src, 'rb').read()
    decompressed_data = zlib.decompress(data)
    open(dst, 'wb').write(decompressed_data)

# compress_file('test.txt', 'test.txt.zlib')
# uncompress_file('test.txt.zlib', 'test.txt.zlib.uncompress')

# data = open('test.txt', 'rb').read()
# compressed_data = lzma.compress(data)
# open('test.txt.lzma', 'wb').write(compressed_data)

# data = open('test.txt.lzma', 'rb').read()
# decompressed_data = lzma.decompress(data)
# open
