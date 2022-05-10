from types import FunctionType
list(FunctionType(list(range(10)),globals())(x=10,y=20))

# globals() = {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 10, 'b': 20, '__file__': 'D:/Users/f_b_r_i_e/Documents/GitHub/Python/QQQQQQQQQQQQ.py', '__cached__': None, 'c': 30, 'd': 40, '__builtin_module_names__': ('posix', 'nt', 'mac', 'os2', 'ce', 'java')}

# FunctionType(list(range(10)),globals())(x=10,y=20) = 40

# list(FunctionType(list(range(10)),globals())(x=
