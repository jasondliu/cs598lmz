import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# new way
obj.__dict__

# new way
type(obj)
obj.__name__

# new way
obj.__class__
obj.__class__.__name__

# new way
obj.__class__.__bases__
obj.__class__.__bases__[0].__name__

# new way
#obj.__class__.__mro__

# new way
obj.__class__.__dict__
obj.__class__.__dict__['name']

# new way
obj.__class__.__dict__['name'].__get__(obj)

# new way
obj.__class__.__dict__['name'].__set__(obj, 'str1')
