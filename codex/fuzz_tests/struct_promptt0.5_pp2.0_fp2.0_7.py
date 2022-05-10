import _struct
# Test _struct.Struct on a 64-bit machine.

import struct
import sys

# We will check the alignment of the structs we create, so we need
# to know the alignment of the basic types.

alignment = {'c': 1,
             'b': 1,
             'B': 1,
             '?': 1,
             'h': 2,
             'H': 2,
             'i': 4,
             'I': 4,
             'l': 4,
             'L': 4,
             'q': 8,
             'Q': 8,
             'f': 4,
             'd': 8,
             's': 1,
             'p': 8,
             'P': 8,
             }

def check_sizeof(fmt, expected):
    s = struct.Struct(fmt)
    got = s.size
    if got != expected:
        print 'Error in sizeof(%s): expected %d, got %d' % (fmt, expected, got)

def check_alignment(fmt, expected):
    s = struct.Struct(
