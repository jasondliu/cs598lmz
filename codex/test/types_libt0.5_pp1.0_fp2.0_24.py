import types
types.FunctionType(lambda x:x, globals())

# FunctionType(code, globals, name=None, argdefs=None, closure=None)
# code: code object (required)
# globals: globals dictionary (optional)
# name: function name (optional)
# argdefs: default arguments values (optional)
# closure: tuple of cell objects (optional)
#
# >>> types.FunctionType(lambda x:x, globals())
# <function <lambda> at 0x7f57b7684a60>
# >>> types.FunctionType(lambda x:x, globals(), 'myfunc')
# <function myfunc at 0x7f57b7684ae8>
# >>> types.FunctionType(lambda x:x, globals(), 'myfunc', (1,))
# <function myfunc at 0x7f57b7684b70>
# >>> types.FunctionType(lambda x:x, globals(), 'myfunc', (1,), (1,))
# Traceback (most recent call last):
#   File "<stdin>", line 1,
