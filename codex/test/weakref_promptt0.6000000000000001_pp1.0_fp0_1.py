import weakref
# Test weakref.ref
class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

f = Foo('an object')
r = weakref.ref(f)

print('f is', f)
print('r is', r)
print('r() is', r())
print('r() is', r() is f)
print()

f = None
print('f is', f)
print('r is', r)
print('r() is', r())
print()

print('r() is', r() is f)
print()

# Test weakref.WeakSet
class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

f = Foo('an object')
s = weakref.WeakSet([f])

print('f is', f)
