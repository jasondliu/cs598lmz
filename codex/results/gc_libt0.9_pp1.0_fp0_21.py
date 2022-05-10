import gc, weakref, sys
#print(dir(gc)) # to discover what you can count for

class A:
    def __del__(self):
        print('A.__del__')
a = A()
wref = weakref.ref(a)
print('before:', sys.getrefcount(a))

wref() # produces None if a was collected
r = wref()
r is None
del a
gc.collect()

print('after:', sys.getrefcount(a)) # after a is deleted, you can see the count is 1
a = wref() # a is None too
a is None


class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass({!r})'.format(self.name)
a = MyClass('a')
b = MyClass('b')
a.b = b
b.a = a
print('a:', sys.getrefcount(a))
del a
del b

gc.garbage
gc.collect()
