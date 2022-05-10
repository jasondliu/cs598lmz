import weakref
# Test weakref.ref() on an object with a __del__ method.
class MyObject(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'MyObject(%r)' % self.name

    def __del__(self):
        print 'deleting %r' % self


def callback(r):
    print 'callback(%r)' % r


obj = MyObject('obj')
r = weakref.ref(obj, callback)
print 'obj:', obj
print 'reference:', r
print 'r():', r()
print 'deleting obj'
del obj
print 'r():', r()
