import lzma
lzma_type = type(lzma.LZMADecompressor())

from .exceptions import DecodingError
from .exceptions import ResolvesToEmpty
from .exceptions import StopDecoding
from .exceptions import ValidationError
from . import extra
from . import fallback
from . import passes

from . import raw
from .raw import map  # noqa: F401


def stream_xz(stream, **kwargs):
    if isinstance(stream, bytes):
        return fallback.stream_xz(stream, **kwargs)
    else:
        return lzma.open(stream, 'rb', **kwargs)


def stream_zlib(stream, **kwargs):
    if isinstance(stream, bytes):
        return fallback.stream_zlib(stream, **kwargs)
    else:
        return zlib.decompressobj()


def stream_raw(stream, **kwargs):
    return stream


def stream_gzip(stream, **kwargs):
    if isinstance(stream, bytes):
        return fall
