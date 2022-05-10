import _struct
# Test _struct.Struct
from _struct import *

try:
    str
except NameError:
    str = str

unpacked_data = (
    # invalid format
    (b"abcdefgh", "!", 0, error, None),
    # single format, too short
    (b"abcdefgh", "b", 0, error, None),
    # single format, exact length
    (b"abcdefgh", "b", 1, 1, b"a"),
    # single format, too long
    (b"abcdefgh", "b", 2, error, None),
    # format with count, too short
    (b"abcdefgh", "3b", 0, error, None),
    # format with count, exact length
    (b"abcdefgh", "3b", 3, 3, b"abc"),
    # format with count, too long
    (b"abcdefgh", "3b", 4, error, None),
    # pointer to integer
    (b"abcdefgh", "b", 1, 1, b"a"),
    (b"abcdefgh", "3
