import ctypes
ctypes.cast(id(int), ctypes.py_object).value
# ctypes.cast(id(int), ctypes.py_object).value is same as sys.modules['__builtin__'].int

# The builtin module is not directly accessible by name (except for __builtin__ in Python 2.X), but it can be
# accessed through the modules dictionary in sys.modules, and its attributes are accessible through the __dict__
# attribute of any module, class, or instance:

import sys
print(sys.modules['__builtin__'])
print(sys.modules['__builtin__'].int)
print(int.__dict__['__dict__'])
print(int.__dict__['__dict__'].__class__)

# The built-in scope is a module, but it is not a normal module because it is created by the interpreter itself,
# and not by an import statement.

# The built-in scope is implemented as a module object in the Python/C API, but the module object does not have
# a __dict__ attribute. The built-in scope is implemented as a
