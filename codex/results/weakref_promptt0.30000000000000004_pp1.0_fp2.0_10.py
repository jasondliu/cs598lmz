import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, name):
        self.name = name
        print 'Created', self.name
    def __del__(self):
        print 'Deleted', self.name

def callback(r):
    print 'callback', r()

a = Foo('a')
r = weakref.ref(a, callback)
print 'made ref', r
print 'deleting a'
del a
print 'a is gone'
print 'r() is', r()
print 'deleting r'
del r
print 'r is gone'
