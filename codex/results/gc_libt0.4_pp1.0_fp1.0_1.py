import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

obj = MyClass('obj')
r = weakref.ref(obj)
print 'obj:', obj
print 'ref:', r
print 'r():', r()

print 'deleting obj'
del obj
print 'r():', r()

obj = MyClass('obj')
p = weakref.proxy(obj)
print 'obj:', obj
print 'proxy:', p
print 'p.name:', p.name

print 'deleting obj'
del obj
print 'p.name:', p.name
