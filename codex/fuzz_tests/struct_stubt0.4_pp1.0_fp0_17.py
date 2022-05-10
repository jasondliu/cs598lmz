from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# namedtuple
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
my_car = Car('red', 3812.4)
my_car.color
my_car.mileage

# deque
from collections import deque
d = deque('ghi')
for elem in d:
    print(elem.upper())
d.append('j')
d.appendleft('f')
d.pop()
d.popleft()
list(d)

# defaultdict
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

# OrderedDict
from collections import OrderedD
