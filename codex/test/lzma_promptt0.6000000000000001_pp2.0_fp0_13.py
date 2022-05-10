import lzma
# Test LZMADecompressor by decompressing all data in `data`.
# Return the decompressed data.

def decompress(data):
    d = lzma.LZMADecompressor()
    return d.decompress(data)

def decompress_iter(data):
    d = lzma.LZMADecompressor()
    return d.decompress(data)
def decompress_file(filename):
    with open(filename, 'rb') as f:
        decompressor = lzma.LZMADecompressor()
        with open(filename.replace('.xz', ''), 'wb') as out_file:
            for buf in iter(partial(f.read, 4096), b''):
                out_file.write(decompressor.decompress(buf))
            out_file.write(decompressor.flush())
