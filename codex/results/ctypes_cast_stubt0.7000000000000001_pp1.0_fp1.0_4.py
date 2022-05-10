import ctypes
ctypes.cast(id(self), ctypes.py_object).value

#now you can change the value of self
#but watch out, this is dangerous...
</code>

