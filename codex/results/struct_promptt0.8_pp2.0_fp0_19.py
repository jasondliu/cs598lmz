import _struct
# Test _struct.Struct.unpack()
#
# Surprisingly, some things that C's unpack would consider an error,
# Python's _struct.Struct.unpack() accepts and just overwrites the
# target fields appropriately.
import _testcapi
import array
import unittest
import sys
import math

# This list contains the values used to test the 'internals'
# of the unpacker.  The test_struct testcases below check
# the behaviour against python values.
#
# The following types are tested:
#
#   b   - signed char
#   B   - unsigned char
#   h   - short
#   H   - unsigned short
#   i   - int
#   I   - unsigned int
#   l   - long
#   L   - unsigned long
#   f   - float
#   d   - double
#   q   - long long
#   Q   - unsigned long long
#   s   - char[]
#   p   - char[]
#   P   - void *
#
# for each, a test value and the byte representation across 4
# different byte orders
