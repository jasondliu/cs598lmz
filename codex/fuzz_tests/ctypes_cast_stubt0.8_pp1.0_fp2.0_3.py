import ctypes
ctypes.cast(0, ctypes.py_object)
 
# prints "<class 'ctypes.py_object'>"
print(ctypes.cast(0, ctypes.py_object).__class__)
 
obj1 = ctypes.py_object(obj)
 
# equivalent to "obj1 = obj"
obj1.value
 
# prints "<class '__main__.Spam'>"
print(obj1.value.__class__)
 
obj2 = ctypes.cast(obj1, ctypes.py_object)
 
# equivalent to "obj2 = obj1"
obj2.value
 
# prints "<class '__main__.Spam'>"
print(obj2.value.__class__)
