import weakref
# Test weakref.reference
import operator
import gc
class MyBase:
    pass
class MyKlass(MyBase):
    pass
def f(x):
    return x.value + 1
def g(x):
    return x.value + 2
class MyWeak:
    def __init__(self, value):
        self.value = value
    def __call__(self):
        return self.value
    def __hash__(self):
        return 1
class MyStr:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __hash__(self):
        return hash(self.value)
class MyInt:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __hash__(self):
        return hash(self.value)
# Initialize a few objects
w1 = MyWeak(1)
w2 = MyWeak(2)
