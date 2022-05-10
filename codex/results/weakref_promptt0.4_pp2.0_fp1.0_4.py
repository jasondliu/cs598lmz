import weakref
# Test weakref.ref() and weakref.proxy()

import weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

o = MyClass('instance')
r = weakref.ref(o)
p = weakref.proxy(o)

print 'o   :', o
print 'r   :', r
print 'p   :', p
print 'r():', r()
print 'p.name:', p.name

print 'deleting o'
del o
print 'r():', r()
print 'p.name:', p.name
