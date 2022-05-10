import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
        print('Creating a Foo')
    def __del__(self):
        print('Destroying a Foo')

def bar():
    print('Creating a Bar')
    f = Foo('f')
    wr = weakref.ref(f)
    print('Created a weak reference to f')
    print(wr)
    f = None
    print('After f = None')
    print(wr)
    print('Before explicit gc.collect()')
    gc.collect()
    print('After explicit gc.collect()')
    print(wr)

bar()
# Test weakref.WeakValueDictionary

class Foo:
    def __init__(self, name):
        self.name = name
        print('Creating a Foo')
    def __del__(self):
        print('Destroying a Foo')

def bar():
    print('Creating a Bar')
    f = Foo('f')
    wvd = weakref.WeakValueDictionary()
   
