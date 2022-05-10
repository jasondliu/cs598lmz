from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = get_decompress(BZ2Decompressor, BZ2_MAGIC)

from lzma import LZMADecompressor
LZMADecompressor.decompress = get_decompress(LZMADecompressor, LZMA_MAGIC)

from zlib import Decompress
Decompress.decompress = get_decompress(Decompress, ZLIB_MAGIC)


def is_compressed(fname):
    """Check if file is compressed

    Parameters
    ----------
    fname : str
        name of the file to check

    Returns
    -------
    compressed : bool
        True if compressed, False otherwise
    """
    return os.path.splitext(fname)[1] in ALLOWED_EXTENSIONS
