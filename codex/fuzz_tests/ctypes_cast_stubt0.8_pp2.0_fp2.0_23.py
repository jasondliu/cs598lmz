import ctypes
ctypes.cast(id(store), ctypes.py_object).value = None  # store dies

# No more checks.
x.value = 5
x.value = -2  # allow negative

del x
del store
 
# Create an object to track.
class TrackedInt(object):

    def __init__(self, name, value=0):
        self.__name = name
        self.__value = value

    def _set(self, value):
        """Set the value, and print a message."""
        if not isinstance(value, int):
            raise TypeError('Expected int, got %r' % value)
        if value < 0:
            raise ValueError('Cannot be negative')
        self.__value = value
        print self.__name, '=', self.__value

    # No delete attribute.

    value = property(fset=_set)

# Create a reference to the TrackedInt object.
x = TrackedInt('x')
# Modify x.value, printing a message each time.
x.value = 1
x.value
