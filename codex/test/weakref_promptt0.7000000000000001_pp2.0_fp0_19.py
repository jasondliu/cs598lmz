import weakref
# Test weakref.ref() with a class

class C:
    pass

def callback(x):
    print('callback(', x, ')')

def test1():
    x = C()
    r = weakref.ref(x, callback)
    print('created', r)
    print('deleting x')
    del x
    callback(r)
    print('getting r')
    print('r() is', r())
    print('done')

# Test weakref.ref() with a class, with some methods overridden

class C:
    def __init__(self, arg):
        self.arg = arg
    def __repr__(self):
        return 'C(%r)' % self.arg
    def __eq__(self, other):
        return self.arg == other.arg
    def __hash__(self):
        return hash(self.arg)

def test2():
    x = C(42)
    r = weakref.ref(x, callback)
    print('created', r)
    print('deleting x')
   
