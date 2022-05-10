import gc, weakref

print('\nA simple class')
class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'A(%s)' % self.value
a = A(10)
b = A(20)
c = A(30)
print(a, b, c)
del a, b, c
print()


print('\nA class with a weak reference')
class B:
    def __init__(self, value):
        self.value = value
        self.ref = weakref.ref(value)

    def __repr__(self):
        return 'B(value=%s, ref=%s)' % (self.value, self.ref)

a = A(10)
b = B(a)
c = B(a)
print(b, c)

print('\nCollecting the parent object')
del a
gc.collect()
print(b, c)

print('\nModifying the parent object')
a = A(30)

