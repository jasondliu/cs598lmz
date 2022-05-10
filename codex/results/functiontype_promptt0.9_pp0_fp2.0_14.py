import types
# Test types.FunctionType
t = lambda : 1
assert isinstance(t, types.FunctionType)
print(t)
#=> <function <lambda> at 0x10833b048>

# Test types.LambdaType
assert isinstance(t, types.LambdaType)
print(t)
#=> <function <lambda> at 0x10833b048>

"""
There are the other function types such as generator types:
	- generator,
	- coroutine,
	- coroutine function,
	- generator function,
	- generator wrapper,
	- method wrapper,
	- code wrapper
"""

# Generator functions types
a = (x for x in range(10))
print(a)
#=> <generator object <genexpr> at 0x1083e3ec0>
assert isinstance(a, types.GeneratorType)
print(a)
#=> <generator object <genexpr> at 0x1083e3ec0>

# Coroutine function types

from inspect import iscoroutinefunction, isgeneratorfunction, isfunction

def coroutine():
