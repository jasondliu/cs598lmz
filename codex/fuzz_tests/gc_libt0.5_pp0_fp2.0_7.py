import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

o = MyClass('instance')
r = weakref.ref(o)
print 'o:', o
print 'ref:', r
print 'r():', r()

o2 = MyClass('instance2')
r2 = weakref.ref(o2)
print 'o2:', o2
print 'ref2:', r2
print 'r2():', r2()

del o
print 'o deleted'
print 'r():', r()

del o2
print 'o2 deleted'
print 'r2():', r2()

try:
    print 'r2():', r2()
except ReferenceError:
    print 'r2 is dead'


# 对于那些不支持弱引用的对象，可以使用weakref
