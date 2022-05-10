from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

import sys
sys.getsizeof(s)

import array
a = array.array('i', range(5))
sys.getsizeof(a)

s = Struct('i' * 100)
sys.getsizeof(s)

from timeit import timeit
timeit('Struct("i")', 'from _struct import Struct', number=100000)

timeit('Struct("i" * 100)', 'from _struct import Struct', number=100000)

from timeit import timeit
timeit('array("i", range(100))', 'from array import array', number=100000)

timeit('array("i", [0] * 100)', 'from array import array', number=100000)

import os
os.urandom(10)

import array
numbers = array.array('h', os.urandom(10))
numbers

octets = bytes(numbers)
octets

import struct
struct.unpack('>10h', octets)

with
