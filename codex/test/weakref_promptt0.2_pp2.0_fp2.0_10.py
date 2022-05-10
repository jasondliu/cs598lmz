import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def callback(r):
    print('callback(', r, ')')

f = Foo('f')
r = weakref.ref(f, callback)
print('created object:', f)
print('created ref:', r)
print('r():', r())
print('deleting f')
del f
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())
