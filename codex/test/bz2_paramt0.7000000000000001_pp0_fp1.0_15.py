from bz2 import BZ2Decompressor
BZ2Decompressor

def BZ2File(filename, mode='r', buffering=1):
    """Open a bzip2 file.

    Return a file object.  The mode can be 'r' or 'w'.  The file will
    be automatically closed when it is garbage collected.
    """
    return BZ2CompressorFile(file(filename, mode, buffering), mode)

