import weakref
# Test weakref.ref() with classes and methods.
import weakref

class MyObject(object):

    def __init__(self, name):
        self.name = name

    def get(self):
        return self.name


# We test that a .__get__() cached on an instance method
# weakref doesn't prevent its deletion

obj = MyObject('obj')
def f1(x, y):
    return x+y

w1 = weakref.ref(f1)
wr = weakref.ref(obj.get)
del f1
f = wr()
assert f() == 'obj'

class Outer(MyObject):

    def get(self):
        return self.name

    def f2(self, x, y):
        return x+y

    outer_attr = f2

obj = Outer('obj')
w1 = weakref.ref(Outer.f2)
wr = weakref.ref(obj.get)
del Outer
w2 = weakref.ref(obj.outer_attr)
assert wr() == 'obj'
assert w1() ==
