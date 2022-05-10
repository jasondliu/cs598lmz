import ctypes
ctypes.cast(p, ctypes.py_object).value

# Convert a function to a callable object with types.MethodType()
# https://docs.python.org/3/library/types.html#types.MethodType
import types
def foo(self, arg):
    return self + arg

class A:
    pass

a = A()
a.foo = types.MethodType(foo, a)
a.foo(1)

# Convert a function to a callable object with operator.methodcaller
# https://docs.python.org/3/library/operator.html#operator.methodcaller
import operator
operator.methodcaller('foo', 1)(a)

# Call a function and ignore its return value with contextlib.suppress
# https://docs.python.org/3/library/contextlib.html#contextlib.suppress
# https://docs.python.org/3/library/exceptions.html#exceptions.FileNotFoundError
# https://docs.python.org/3/library/os.html#os.remove
import contextlib
contextlib.suppress
