import weakref
# Test weakref.ref() on instances

class Foo(object):
    pass

def bar():
    pass

inst = Foo()
wr = weakref.ref(inst)
print wr() is inst

inst = Foo()
wr = weakref.ref(inst, bar)
print wr() is inst

func = Foo()
func.__call__ = lambda: 5
wr = weakref.ref(func)
print wr().__call__()

class Foo(object):
    pass

def bar1():
    pass
def bar2():
    pass

inst = Foo()
wr = weakref.ref(inst, bar1)
print wr() is inst

wr = weakref.ref(inst, bar2)
print wr() is inst

wr = weakref.ref(inst)
print wr() is inst
# Test weakref.ref() on classic classes

class Foo:
    pass

def bar():
    pass

inst = Foo()
wr = weakref.ref(inst)
print wr() is inst

inst = Foo()
wr = weakref.ref(inst,
