from types import FunctionType
list(FunctionType(lambda: 1, {}, '', (), None))

# FunctionType
#   __init__(self, code, globals, name, argdefs, closure)
#   __call__(self, *args, **kwds)
#   __get__(self, obj, objtype)
#   __repr__(self)
#   __str__(self)
#   __getattribute__(self, name)
#   __eq__(self, other)
#   __ne__(self, other)
#   __hash__(self)
#   __reduce__(self)
#   __reduce_ex__(self, protocol)
#   __doc__
#   __name__
#   __dict__
#   __module__
#   __defaults__
#   __code__
#   __closure__
#   __kwdefaults__
#   __annotations__
#   __globals__
