import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
weakref.ref(a,callback)
lst.append(a)

# Test issue #5239: weakref.ref() should call the callback with the
# reference as an argument.

class Callback:
    def __init__(self):
        self.called = False
    def __call__(self, wr):
        self.called = True
        self.wr = wr

class Obj(object):
    pass

wr = weakref.ref(Obj(), Callback())
assert wr.__class__ is weakref.ReferenceType
assert wr() is None
assert wr.called
assert wr.wr() is None
assert wr.wr is wr

# Test issue #5239 (part 2): weakref.ref(obj, None, ...) should return
# a proxy for obj, not a reference to it.

class Obj2(object):
    pass

wr = weakref.ref(Obj2(), None, Callback())
assert wr.__class__ is Obj2
assert wr
