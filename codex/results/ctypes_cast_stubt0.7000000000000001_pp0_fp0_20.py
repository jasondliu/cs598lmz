import ctypes
ctypes.cast(id(x), ctypes.py_object).value is x

# get the reference count of an object
import sys
sys.getrefcount(x)

# set the number of references
sys.getrefcount(x) = 10

# get the size of an object (in bytes)
sys.getsizeof(x)

# get the type of an object
type(x)
isinstance(x, int)

# check if an object has a specific type

# create a new object
# object()

# convert an object to string
x = "foo"
str(x)

# print an object
print x

# delete an object
del x

# copy an object
import copy
copy.copy(x)

# deep copy an object
copy.deepcopy(x)

# create an empty object
object()

# determine if an object is callable
class Dummy:
    def foo(self):
        pass

d = Dummy()
callable(d.foo)

d

# call an object
d.foo()


