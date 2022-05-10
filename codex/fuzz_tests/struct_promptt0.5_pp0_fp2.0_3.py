import _struct
# Test _struct.Struct

import unittest
from test import test_support
from test.test_support import bigaddrspacetest

import sys
import struct
import array
import math

# Some structs to test with

# (format, value, big-endian, little-endian)

tests = [
    ('b', 127, '\177', '\177'),
    ('B', 255, '\377', '\377'),
    ('B', 0, '\000', '\000'),
    ('h', 32767, '\177\377', '\377\177'),
    ('H', 65535, '\377\377', '\377\377'),
    ('H', 0, '\000\000', '\000\000'),
    ('i', 2147483647, '\177\377\377\377', '\377\377\377\177'),
    ('I', 4294967295L, '\377\377\377\377', '\377\377\377\377'),
    ('I', 0, '\000\000\000\000', '\
