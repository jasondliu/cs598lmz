from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

# __code__
# __code__ is a read-only attribute that returns a code object representing the compiled function body.
#
# >>> def f(): pass
# ...
# >>> f.__code__
# <code object f at 0x7f5d0b9d0d20, file "<stdin>", line 1>
# >>> f.__code__.co_name
# 'f'
# >>> f.__code__.co_varnames
# ()
# >>> f.__code__.co_argcount
# 0
# >>> f.__code__.co_filename
# '<stdin>'
# >>> f.__code__.co_firstlineno
# 1
# >>> f.__code__.co_flags
# 67

