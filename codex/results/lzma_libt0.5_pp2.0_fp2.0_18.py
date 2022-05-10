import lzma
lzma.LZMA_AVAILABLE = True

from .base import BaseCompressor, BaseDecompressor
from .utils import (
    Base64Decoder,
    Base64Encoder,
    Base85Decoder,
    Base85Encoder,
    BZ2Compressor,
    BZ2Decompressor,
    GzipCompressor,
    GzipDecompressor,
    LZMACompressor,
    LZMADecompressor,
    ZlibCompressor,
    ZlibDecompressor,
)

if lzma.LZMA_AVAILABLE:
    from .lzma import LZMACompressor, LZMADecompressor

COMPRESSORS = {
    "b64": (Base64Encoder, Base64Decoder),
    "b85": (Base85Encoder, Base85Decoder),
    "bz2": (BZ2Compressor, BZ2Decompressor),
    "gz": (GzipCompressor, GzipDecompressor),
    "lzma": (LZMAComp
