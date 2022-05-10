import weakref
# Test weakref.ref(x, f)
class Foo(object):
    def __init__(self, name):
        self.name = name

def callback(x):
    print 'dead:', x.name

def test_callback():
    f = Foo('foo')
    x = weakref.ref(f, callback)
    print x, x()
    del f
    print x, x()
    print 'end of test'

test_callback()
