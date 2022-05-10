import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()

class A:
    pass
x=[]

for i in range(100):
    a = A()
    x.append(a)

for a in x:
    assert gc.collectable(a)

# test GC of weakrefs
from weakref import *
from UserList import UserList
from UserString import UserString

def test_UserList():
    def kill(obj):
        obj.append(obj)
        del obj[0]

    u = UserList()
    wr = ref(u, kill)
    wr()
    u.append(wr)
    u = None
    gc.collect()
    assert wr() is None

def test_UserDict():
    def kill(obj):
        obj[1] = 2
        obj[2] = 1

    u = UserDict()
    wr = ref(u, kill)
    wr()
    u[wr] = 1
    u = None
    gc.collect()
    assert wr() is None

def test_UserString():
    def kill
