import weakref
# Test weakref.ref() with a cyclic linked list.
import sys
import weakref


class A:
    pass


a = A()
a.next = a


def b(arg):
    pass


class MyWeakref(weakref.ref):

    def __init__(self, ob):
        self.c = []
        weakref.ref.__init__(self, ob)

    def __call__(self):
        self.c.append(1)
        return weakref.ref.__call__(self)


class MyCallableWeakref(MyWeakref):

    def __call__(self):
        self.c.append(2)
        return MyWeakref.__call__(self)


r = MyWeakref(a)
r2 = MyWeakref(a)
r3 = MyWeakref(b)
r4 = MyCallableWeakref(b)
r5 = MyCallableWeakref(b)
b_id = id(b)
del a, b
if r() is not None:
    raise RuntimeError
if r2() is
