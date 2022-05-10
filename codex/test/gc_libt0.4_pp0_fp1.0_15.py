import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

# Create a reference cycle
a = MyClass('a')
b = MyClass('b')
a.b = b
b.a = a

# Create a weak reference to a
a_ref = weakref.ref(a)

# Remove the last reference to a
del a
del b

# a_ref is still alive because it is a weak reference
print(a_ref)

# a_ref is dead because there are no strong references to the object
gc.collect()
print(a_ref)

# Output:
# <weakref at 0x7f6f0b6b0e80; to 'MyClass' at 0x7f6f0b6b0c40>
# None
