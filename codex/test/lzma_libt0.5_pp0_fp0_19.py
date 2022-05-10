import lzma
lzma.LZMA_ERROR_FORMAT = 1

import os
import sys

def msdosify(filename):
    """Replace the current file with a MSDOS-friendly version."""
    f = open(filename, 'rb')
    data = f.read()
    f.close()
    f = open(filename, 'wb')
    f.write(data.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n'))
    f.close()

def unixify(filename):
    """Replace the current file with a Unix-friendly version."""
    f = open(filename, 'rb')
    data = f.read()
    f.close()
    f = open(filename, 'wb')
    f.write(data.replace(b'\r\n', b'\n'))
    f.close()

def lzma_compress(filename):
    """Replace the current file with an LZMA-compressed version."""
