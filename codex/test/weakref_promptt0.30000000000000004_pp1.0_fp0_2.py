import weakref
# Test weakref.ref() on a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('callback'))
print(r2)
print(r2())

del o2
gc.collect()
print(r2())

# Test weakref.ref() on a class instance with a __del__ method.

class D:
    def __del__(self):
        print('D.__del__')

o = D()
r = weakref.ref(o)
print(r)
print(r())

o2 = D()
r2 = weakref.ref(o2, lambda x: print('callback'))
print(r2)
print(r2())

del o2
gc.collect()
print(r2())

# Test weakref.ref() on a class instance with a __del__ method that raises
# an exception.

