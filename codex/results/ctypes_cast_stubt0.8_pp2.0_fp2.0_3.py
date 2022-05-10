import ctypes
ctypes.cast(p ,ctypes.py_object).value

# p = ctypes.cast(id(obj),ctypes.c_void_p)

# 1. a c_void_p instance holds a void pointer, which is just a pointer to a memory location that doesn't have a
# defined type.
# 2. converting an object to a c_void_p returns the memory address of the object (just like id(obj) would)
# 3. "reversing" it (ctypes.cast(123, ctypes.py_object).value) returns the object stored at that location
# 4. this only works when the object is still stored in memory, otherwise it raises:
# ctypes.ArgumentError: argument 2: : don't know how to convert parameter 2


# copy.copy(obj)
# create shallow copy of object
# also obj.copy() method
# eg. t1 = t.copy(); only outer list is copied


# copy.deepcopy(obj)
# make deep copy of object
# eg. t2 = copy.deepcopy(t)


# copy.copy() # create shallow
