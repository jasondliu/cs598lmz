fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()


# =======================================================
from collections import namedtuple
class A:
    __slots__ = ()
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
a = A(1, 2, 3)
b = A(4, 5, 6)
print(a)
print(b)

print('\n-----------')
Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(100, 150, 2000)
print(p)
print(p.x)
print(p.y)
print(p.z)
print(p[0])
print(p[1])
print(p[2])

# ===============================================
from collections import deque, defaultdict, OrderedDict, Counter

__slots__ = ('name', 'age', 'gender')
def fn():
    print('hello')

q = deque([1, 2, 3])
print(hasattr(q
