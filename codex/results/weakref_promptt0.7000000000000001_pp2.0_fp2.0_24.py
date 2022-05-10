import weakref
# Test weakref.ref.__call__
class C:
    pass

obj = C()
r = weakref.ref(obj)
obj2 = r()
obj == obj2

class D(C):
    pass

obj3 = D()
r2 = weakref.ref(obj3)
obj4 = r2()
obj3 == obj4

# Test weakref.ref.proxy
import operator

class E:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'E(' + repr(self.value) + ')'
    def __eq__(self, other):
        return self.value == other
    def __lt__(self, other):
        return self.value < other
    def __add__(self, other):
        return E(self.value + other)
    def __radd__(self, other):
        return E(other + self.value)
    def __mul__(self, other):
        return E(self.value * other)
    def __rmul__
