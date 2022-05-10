import weakref
# Test weakref.ref(obj)

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'Goodbye, %s' % self.name

f = Foo('Alex')
r = weakref.ref(f)
print r
print r()
print f is r()
print f == r()
print f.name
print r().name

del f
print r()
print r() is None

print r() == None

# Test weakref.ref(obj, callback)

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'Goodbye, %s' % self.name

f = Foo('Alex')
def callback(r):
    print '%s has been deleted' % r().name
r = weakref.ref(f, callback)
print r
print r()
print f is r()
print f == r()
print f.name
print r().name

del f
print
