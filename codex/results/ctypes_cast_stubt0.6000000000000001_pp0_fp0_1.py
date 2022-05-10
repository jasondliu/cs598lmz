import ctypes
ctypes.cast(id(my_dict), ctypes.py_object).value

my_dict['x'] = 10

# set ref_count to 1 to avoid garbage collection
ctypes.cast(id(my_dict), ctypes.py_object).value

# create a reference to my_dict
another_dict = my_dict

# now, both `my_dict` and `another_dict` refer to the same object
# the reference count is 2
ctypes.cast(id(my_dict), ctypes.py_object).value

# delete the `another_dict` reference
del another_dict

# my_dict is still around, so the object count is 1
ctypes.cast(id(my_dict), ctypes.py_object).value

# delete the my_dict reference
del my_dict

# as there are no more references to the object, it gets destroyed
# and its reference count goes to zero
ctypes.cast(id(my_dict), ctypes.py_object).value

# the next line will raise an error, as the object does not exist anymore
my
