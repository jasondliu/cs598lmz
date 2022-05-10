import ctypes
ctypes.cast(id(my_dict), ctypes.py_object).value

# 方法二
my_dict.__dict__

# 方法三
type.__getattribute__(my_dict, '__dict__')

# 方法四
my_dict.__class__.__dict__['__dict__'].__get__(my_dict)

# 方法五
my_dict.__class__.__dict__['__dict__'].__get__(my_dict, type(my_dict))

# 方法六
my_dict.__class__.__dict__['__dict__'].__get__(my_dict, my_dict.__class__)

# 方法七
my_dict.__class__.__dict__['__dict__'].__get__(my_dict, dict)

# 方法八
my_dict.__class__.__dict__['__dict__'].__get__(my_dict, object)
