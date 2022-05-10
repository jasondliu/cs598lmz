from lzma import LZMADecompressor
LZMADecompressor.check = check

from gzip import (
    GzipFile,
    compress as _gzip_compress,
    decompress as _gzip_decompress,
)


def gzip_compress(data, compresslevel=9):
    """gzip_compress(data: bytes, compresslevel: int = 9) -> bytes

    Compress data. If data is unicode, convert it to bytes first.
    """
    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    return _gzip_compress(data, compresslevel)


def gzip_decompress(data):
    """gzip_decompress(data: bytes) -> bytes

    Decompress data. Return bytes.
    """
    return _gzip_decompress(data)


def gzip_open(filename, mode='rb'):
    """open(filename: str, mode: str = 'rb') -> GzipFile

    Open a gzip-compressed file in binary or text mode.
    The filename argument can be an actual filename
