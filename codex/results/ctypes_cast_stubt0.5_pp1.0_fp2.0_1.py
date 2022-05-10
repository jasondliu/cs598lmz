import ctypes
ctypes.cast(id(my_dict), ctypes.py_object).value

# 方法2
my_dict.__dict__ 

# 方法3
vars(my_dict)

# 方法4
type.__dict__['__dict__'].__get__(my_dict)()

# 方法5
type.__dict__['__dict__'].__get__(my_dict)

# 方法6
type.__dict__['__dict__'].__get__(my_dict)()

# 方法7
type.__dict__['__dict__'].__get__(my_dict)()

# 方法8
type.__dict__['__dict__'].__get__(my_dict)()

# 方法9
type.__dict__['__dict__'].__get__(my_dict)()

# 方法10
type.__dict__['__dict__'].__get__(my_
