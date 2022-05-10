import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

try:
    from zlib import compress as zlib_compress
    from zlib import decompress as zlib_decompress
    zlib_available = True
except ImportError:
    zlib_available = False

from acoustid.compat import BytesIO
from acoustid.data import parse_version_string


def _decompress_from_bytes(data, decompress):
    in_buffer = BytesIO(data)
    out_buffer = BytesIO()
    while True:
        buf = in_buffer.read(8192)
        if not buf:
            break
        buf = decompress(buf)
        out_buffer.write(buf)
    return out_buffer.getvalue()


def decompress_from_bytes(data, compression_method=None):
    if compression_method is None:
        compression_method = data[0:2]
        data = data[2:]
    if compression_method ==
