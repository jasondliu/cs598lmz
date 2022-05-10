from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('@I=I')
s.size
s.format
s.unpack(b'\x00\x00\x00\x00\x00\x00\x00\x00')

import struct
struct.pack('@I=I', 1, 2)

import sys
sys.getsizeof(s)

import array
array.array('i', (1, 2, 3))

import collections
collections.namedtuple('Point', ['x', 'y'])

import bisect
bisect.bisect([1, 2, 3], 2)
bisect.bisect_left([1, 2, 3], 2)
bisect.bisect_right([1, 2, 3], 2)

import heapq
h = [1, 2, 3]
heapq.heappush(h, 4)
h
heapq.heappop(h)
h
heapq.heappushpop(h, 5)
h
heapq.heapreplace(h, 6)
h

import it
