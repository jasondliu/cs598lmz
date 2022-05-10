import weakref
# Test weakref.ref() on instances

class Foo(object):
    pass

def bar():
    pass

inst = Foo()
wr = weakref.ref(inst)
