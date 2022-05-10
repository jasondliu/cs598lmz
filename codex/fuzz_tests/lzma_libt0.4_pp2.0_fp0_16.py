import lzma
lzma.LZMAFile

from . import lzma_compat

from .lzma_compat import LZMAFile

__all__ = [
    'LZMAFile',
]
