import lzma
lzma_decompress = lzma.decompress

def lzma_compress(data):
    with lzma.open(
            'asdf.xz',
            'wb',
            format=lzma.FORMAT_ALONE,
            check=lzma.CHECK_NONE,
            preset=9
    ) as f:
        f.write(data)
    with open('asdf.xz', 'rb') as f:
        return f.read()

