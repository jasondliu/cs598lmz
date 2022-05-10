from types import FunctionType
list(FunctionType(f, globals(), 'f') for f in [lambda: 1, lambda: 2])

# $ python3 -c 'from types import FunctionType; list(FunctionType(f, globals(), "f") for f in [lambda: 1, lambda: 2])'
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# TypeError: function() argument 1 must be code, not function

# $ python2 -c 'from types import FunctionType; list(FunctionType(f, globals(), "f") for f in [lambda: 1, lambda: 2])'
# [<function f at 0x7f8e566fa320>, <function f at 0x7f8e566fa398>]
# $ python2 -c 'from types import FunctionType; list(FunctionType(f, globals(), "f") for f in [lambda: 1, lambda: 2])[0]()'
# 1
# $ python2 -c 'from types import FunctionType; list(FunctionType(f, globals(), "f") for f in [lambda:
