from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Using the struct module to unpack data
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
data
struct.unpack('>i4sh', data)

# Using the array Module
from array import array
a = array('i', [1, 2, 3, 4])
a

# Using the collections Module
from collections import deque
d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print('Handling', d.popleft())

# Using the heapq Module
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
[heappop(data) for i in range(3)]

# Using the bisect Module
from bisect import bisect
HAYSTACK = [1, 4, 5, 6, 8, 12,
