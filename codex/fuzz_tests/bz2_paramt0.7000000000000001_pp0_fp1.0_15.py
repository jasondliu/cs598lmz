from bz2 import BZ2Decompressor
BZ2Decompressor

def BZ2File(filename, mode='r', buffering=1):
    """Open a bzip2 file.

    Return a file object.  The mode can be 'r' or 'w'.  The file will
    be automatically closed when it is garbage collected.
    """
    return BZ2CompressorFile(file(filename, mode, buffering), mode)

def open(filename, mode="rb", compresslevel=9):
    """Open a bzip2-compressed file in binary or text mode.

    The filename argument can be an actual filename (a str or bytes object), or
    an existing file object to read from or write to.

    The mode argument can be "r", "rb" for reading (default), "w", "wb" for
    overwriting, "x", "xb" for exclusive creation, or "a", "ab" for appending.
    These can equivalently be given as "rt", "wt", "xt", "at" for text, and
    "rb", "wb", "xb", "ab" for binary.

    The compresslevel argument is an integer from
