from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(b'<2s3s')
s.unpack(b'\x01\x02\x03\x04\x05\x06')

# 2.2.2
from collections import namedtuple
TestResults = namedtuple('TestResults', ['failed', 'attempted'])
t = TestResults(failed = 4, attempted = 5)
t.failed
t.attempted

# 2.2.3
from _collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['a']

# 2.2.4
from _collections import deque
d = deque(range(5))
d.append(5)
d.appendleft(6)
d

# 2.2.5
from _heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heap
