import weakref
# Test weakref.ref() with a class that has a __del__ method.
# This used to crash the interpreter.
import warnings


class A:

    def __del__(self):
        pass


a = A()
r = weakref.ref(a)
warnings.simplefilter('ignore', DeprecationWarning)
r()
warnings.resetwarnings()
del a
import gc
gc.collect()
print(r())
#
# Test weakref.ref() with a class that has a __hash__ method.
# This used to crash the interpreter.
#

#
# Test weakref.ref() with a class that has a __cmp__ method.
# This used to crash the interpreter.
#


class A:

    def __cmp__(self, other):
        return 0


a = A()
r = weakref.ref(a)
warnings.simplefilter('ignore', DeprecationWarning)
r()
warnings.resetwarnings()
del a
import gc
gc.collect()
print(r())
#
# Test weakref.ref() with a class
