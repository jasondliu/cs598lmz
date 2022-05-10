import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# Why is that?

# In Python, there is a lot more going on than in optimized code.
#
# - Variables are pointers to objects, not the objects themselves
# - Every object has a type
# - Every object has a reference count
# - Objects are deallocated when the reference count reaches zero
#
# As a result, some variables need more space than others.

# In C, there are no objects. Variables are the objects.
#
# - Variables are the objects
#
#     int a = 42;    // a is the int
#
# - Variables have a fixed size
#
#     sizeof(int)    // 4 bytes
#
# - Variables are deallocated when they go out of scope

# In Python, objects are the variables.
#
# - Objects are the variables
#
#     a = 42        # 42 is the int
#
# - Objects can be any size
#
#     sys.getsizeof(42)    # 28 bytes
#
# - Objects are deallocated
