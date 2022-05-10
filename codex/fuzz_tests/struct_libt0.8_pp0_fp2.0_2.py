import _struct
from binascii import hexlify

#
# This module provides several functions for dealing with GIF image files.
#
# Example:
#
#     import Image
#     im = Image.open("lenna.gif")
#     im.show()

__version__ = "0.3"

# --------------------------------------------------------------------
# Helpers

i8 = _struct.Struct(">B")
i16 = _struct.Struct(">H")

def get_palette(fp, bits):

    palette = []

    if bits <= 8:
        for i in range(2**bits):
            entry = i8.unpack(fp.read(1))[0]
            palette.append((entry, entry, entry))
    else:
        for i in range(2**bits):
            entry = i8.unpack(fp.read(1))[0]
            palette.append((entry, entry, entry))

    return palette

def get_header(fp):

    header = fp.read(14)

    if len(header) != 14:
        raise
