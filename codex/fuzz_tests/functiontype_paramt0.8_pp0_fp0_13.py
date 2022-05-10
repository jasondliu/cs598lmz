from types import FunctionType
list(FunctionType('lambda x:x','abc'))

# CODE:
# def f(x):
#     return x
# >>> list(FunctionType(f, 'abc'))
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: 'function' object is not iterable
# >>> list(FunctionType(f.__code__, f.__globals__, 'abc', {}))
# ['a', 'b', 'c']

# f = lambda x: x + 1
# >>> f.__code__
# <code object <lambda> at 0x7fc9f65c4e40, file "<stdin>", line 1>
# >>> f.__code__.co_code
# '|\x00|\x01\x17\x00S'
# >>> f.__code__.co_consts
# (None, 1)
# >>> f.__code__.co_names
# ()
# >>> f.__code__.co_varnames
# ('x',)


# >>> f
