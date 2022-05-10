from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

import array
a = array.array('i', xrange(5))
a

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores

from collections import deque
d = deque(xrange(5))
d.append(5)
d.appendleft(6)
d.pop()
d.popleft()
d

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
[heappop(data) for i in range(3)]

from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
round(.70 * 1.05, 2)
Decimal('1.
