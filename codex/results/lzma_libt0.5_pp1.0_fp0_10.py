import lzma
lzma.LZMADecompressor.decompress(data)

# pylint: enable=no-member

# pylint: disable=no-member

def _unpack_xz_file(path):
    """Unpack a xz compressed file.
    """
    with lzma.LZMAFile(path) as fh:
        return fh.read()

# pylint: enable=no-member

def _unpack_xz_stream(stream):
    """Unpack a xz compressed stream.
    """
    with lzma.LZMAFile(None, 'rb', fileobj=stream) as fh:
        return fh.read()

# pylint: disable=no-member

def _unpack_zstd_stream(stream):
    """Unpack a zstd compressed stream.
    """
    return zstd.ZstdDecompressor().decompress(stream)

# pylint: enable=no-member

def _unpack_zstd_file(path):
    """
