import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def bar():
    print('in bar')
    l = [Foo('bar1'), Foo('bar2')]
    a = Foo('bar3')
    wr = weakref.ref(a)
    return wr

def spam():
    print('in spam')
    l = [Foo('spam1'), Foo('spam2')]
    a = Foo('spam3')
    wr = weakref.ref(a)
    return wr

def test():
    print('in test')
    l = [Foo('test1'), Foo('test2')]
    a = Foo('test3')
    wr = weakref.ref(a)
    return wr

wr = test()
print('wr =', wr)
print('deleting wr')
del wr
print('calling gc.collect()')
n = gc.collect()
print
