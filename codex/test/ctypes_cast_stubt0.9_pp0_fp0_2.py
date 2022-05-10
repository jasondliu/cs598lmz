import ctypes
ctypes.cast(0, ctypes.py_object)
#this looks like its the same as the cast we are doing to the py_type ptr, but it works differently. this local variable will point to 0, so the dereference will dereference it to get 0 - which is an invalid pointer.
