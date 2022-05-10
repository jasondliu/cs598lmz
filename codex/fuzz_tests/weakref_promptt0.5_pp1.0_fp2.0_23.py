import weakref
# Test weakref.ref() with a class instance and a __del__ method.
class C:

    def __del__(self):
        print('in C.__del__')
        return

c = C()
r = weakref.ref(c)
print('c:', c)
print('ref:', r)
print('r():', r())
print('deleting c')
del c
print('r():', r())
print('r():', r())
print('r():', r())
print('r():', r())

# Test weakref.ref() with a class instance and a __del__ method that
# raises an exception.  The exception should be swallowed.
class C:

    def __del__(self):
        print('in C.__del__')
        raise RuntimeError

c = C()
r = weakref.ref(c)
print('c:', c)
print('ref:', r)
print('r():', r())
print('deleting c')
del c
print('r():', r())
print('r():', r())
print('r
