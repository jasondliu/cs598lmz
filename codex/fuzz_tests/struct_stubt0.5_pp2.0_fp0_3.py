from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

import sys
sys.getsizeof(s)

from array import array
a = array('I', (0,))
sys.getsizeof(a)

from collections import deque
d = deque(range(10), maxlen=10)
d.appendleft(-1)
d

from collections import defaultdict
dd = defaultdict(list)
dd['a'].append(1)
dd['a'].append(2)
dd['b'].append(4)
dd

from collections import OrderedDict
od = OrderedDict.fromkeys('abcde')
od['a'] = 1
od['d'] = 4
od['b'] = 2
list(od.keys())

from collections import Counter
c = Counter('abracadabra')
c

from heapq import nlargest
nlargest(3, c.values())

from heapq import nsmallest
nsmallest(3, c.values())

import json
d = dict(name='Bob', age=
