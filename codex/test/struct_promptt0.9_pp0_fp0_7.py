import _struct
# Test _struct.Struct with byteorder='<'.
# Test _struct.Struct with byteorder='>'.
# Test _struct.Struct with byteorder='=' and standard size.
# Test _struct.Struct  with byteorder='=' and native size.
# Test _struct.Struct  with byteorder='=' and non-native size.
# Test pack_into
# Test unpack_from
# Test _struct.Struct with byteorder that isn't native, and native size.
# Test pack_into and unpack_from with non-native typesize.
# Test pack_into and unpack_from with non-native typesize (again).
# Test _struct.Struct.format
# Test module docstring
# Test with buffer protocol and memoryview.
import _io
# Test optional __next__ method.
import unittest
import pickle
import sys
import struct
# Ensure struct module matches _struct, for given sizes and alignments
# !!! Depends on being called after the tests for _struct.py !!!
# Equality tests
# Inequality test
# More inequality tests
