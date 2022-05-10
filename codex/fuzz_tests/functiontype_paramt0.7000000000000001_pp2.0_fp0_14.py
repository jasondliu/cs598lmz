from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'f') for x in range(2))

# f_code
#  lambda x: x
# f_globals
#  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': &lt;_frozen_importlib_external.SourceFileLoader object at 0x7f39a26a8f60&gt;, '__spec__': None, '__annotations__': {}, '__builtins__': &lt;module 'builtins' (built-in)&gt;, '__file__': '/home/dive/Projects/build/python-ma-/python-ma-3.6-2.0/build/../../sources/python/Python-3.6.2/Lib/types.py', '__cached__': None, 'FunctionType': &lt;class 'function'&gt;, '__builtin__': &lt;module 'builtins' (built-in)&gt;, 'f': &lt;function f at 0x7f
