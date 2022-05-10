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
