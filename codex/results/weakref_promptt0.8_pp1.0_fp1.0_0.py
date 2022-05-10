import weakref
# Test weakref.ref() and weakref.WeakValueDictionary()

def f(a):
    print 'f() called with', a

class Foo:
    def __init__(self, a):
        self.a = a
        self.b = 'Foo'+a
        print self.b
        
    def __del__(self):
        print 'Foo: deleting', self.b

# test weakref.ref()
# create an instance with a longer life time than the last weak reference
foobar = None

def create_foobar():
    global foobar
    foobar = Foo('bar')
    
def test_ref():
    global foobar
    foobar_ref = weakref.ref(foobar, f)
    del foobar
    foobar = None
    create_foobar()
    del foobar_ref
    
test_ref()

# test weakref.WeakValueDictionary()
# make some instances
class Bar:
    def __init__(self, a):
        self.a = a
        
    def __del__(self):

