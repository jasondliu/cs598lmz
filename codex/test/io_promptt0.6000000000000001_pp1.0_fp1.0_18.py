import io
# Test io.RawIOBase to see if it is a file-like object
# (has a read() method)
#

try:
    f = io.RawIOBase()
    f.read()
except:
    io.RawIOBase = io.IOBase

from numpy import __version__ as numpy_version
from scipy import __version__ as scipy_version
