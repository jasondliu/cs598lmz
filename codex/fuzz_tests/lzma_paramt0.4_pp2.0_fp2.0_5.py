from lzma import LZMADecompressor
LZMADecompressor.__init__

# Decompress a chunk of data.
#
# The *length* argument is only needed for the last chunk of data.
#
# The *unused* argument is only needed to decompress data from
# LZMA.compress().
#
# Returns the uncompressed data.
def decompress(data, length=None, unused=None):
    """
    Decompress a chunk of data.

    The *length* argument is only needed for the last chunk of data.

    The *unused* argument is only needed to decompress data from
    LZMA.compress().

    Returns the uncompressed data.
    """
    pass

# Return the maximum number of bytes needed to decompress the given number
# of bytes.
def max_length(length):
    """
    Return the maximum number of bytes needed to decompress the given number
    of bytes.
    """
    pass

# Return the maximum number of bytes needed to decompress the given number
# of bytes.
def get_max_length(length):
    """
    Return the maximum number of bytes needed
