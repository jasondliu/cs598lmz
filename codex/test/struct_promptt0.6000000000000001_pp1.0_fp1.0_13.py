import _struct
# Test _struct.Struct.
from _struct import Struct

from array import array
from binascii import hexlify
from cStringIO import StringIO
from operator import index
from test import test_support

try:
    from itertools import izip
except ImportError:
    izip = zip

def get_format(St, Sf, T):
    # Try the native format, and if it fails, try the standard format.
    # Return the format that worked.
    try:
        struct.pack(St, 0)
    except struct.error:
        return Sf
    else:
        return St

def get_integer_format(size, le=False, signed=False):
    # Given a size in bytes, return the native and standard format characters
    # for an integer of that size.
    if size == 1:
        St, Sf = 't', 'b' # native, standard
    elif size == 2:
        St, Sf = 'h', 'h'
    elif size == 4:
        St, Sf = 'l', 'l'

