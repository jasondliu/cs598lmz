import ctypes
ctypes.cast(id(int), ctypes.py_object).value
# ctypes.cast(id(int), ctypes.py_object).value is same as sys.modules['__builtin__'].int

# The builtin module is not directly accessible by name (except for __builtin__ in Python 2.X), but it can be
# accessed through the modules dictionary in sys.modules, and its attributes are accessible through the __dict__
# attribute of any module, class, or instance:

import sys
