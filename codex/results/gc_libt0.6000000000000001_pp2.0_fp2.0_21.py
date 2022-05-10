import gc, weakref

class B:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'B(%s)' % self.value

class C:
    def __init__(self):
        self.b = B(42)
    def __repr__(self):
        return 'C()'

def callback(reference):
    print 'callback(', reference, ')'

c = C()
b = c.b
del c
print 'before callback'
r = weakref.ref(b, callback)
print 'after callback'
print 'r:', r
print 'r():', r()
print 'deleting b'
del b
print 'gc.collect():'
gc.collect()
print 'r():', r()
