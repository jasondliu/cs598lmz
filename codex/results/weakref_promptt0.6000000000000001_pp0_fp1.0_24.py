import weakref
# Test weakref.ref() with a class instance.
#
# It is important to test the class with a __del__ method, as the
# behavior of weak references to such objects is tricky.

class C:
    def __del__(self):
        print('deleting', self.__class__.__name__)

class D:
    pass

# The weak reference should not prevent the instance from being
# collected, and the __del__ method should be called when the instance
# is deleted.

c = C()
r = weakref.ref(c)
print(r())
#print(r() is c)
del c
gc.collect()
print(r())
print(c)

# If a class has a __del__ method, it is not safe to create a weak
# reference to an instance of the class.  The object's __del__ method
# may be called before the weak reference object is created, and the
# weak reference may then prevent the instance's __del__ method from
# being called at all.  The behavior of the weak reference is
# undefined if it is created after the instance's
