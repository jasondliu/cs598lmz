from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = decompress

from bz2 import BZ2File
BZ2File.read = read
BZ2File.readline = readline
BZ2File.readlines = readlines

def _bz2_decompress(data):
    """Decompress data using bz2.decompress.
    """
    return BZ2Decompressor().decompress(data)

def _bz2_open(filename, mode):
    """Open a bz2 compressed file.
    """
    return BZ2File(filename, mode)

def _bz2_read(filename):
    """Read a bz2 compressed file.
    """
    return BZ2File(filename, 'rb').read()

def _bz2_readline(filename):
    """Read a line from a bz2 compressed file.
    """
    return BZ2File(filename, 'rb').readline()

def _bz2_readlines(filename):
    """Read lines from a bz2 compressed file.
    """
   
