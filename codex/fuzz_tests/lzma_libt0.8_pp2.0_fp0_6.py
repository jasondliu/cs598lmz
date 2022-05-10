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

try:
    from snappy import SnappyDecompressor
    from snappy import SnappyCompressor
    snappy_compress = SnappyCompressor.compress
    snappy_decompress = SnappyDecompressor.decompress
except ImportError:
    from snappy import snappy_compress
    from snappy import snappy_decompress


@pytest.mark.parametrize(
    'crc_type',
    (
        'xz',
        'none',
        'auto',
        'lzma',
        'l
