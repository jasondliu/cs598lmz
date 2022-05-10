from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# Output:
['__annotations__']
</code>
I've tried using <code>inspect.signature</code> and <code>inspect.getfullargspec</code> to no avail. I've also tried using <code>FunctionType.__code__.co_varnames</code> and <code>FunctionType.__code__.co_argcount</code> to no avail.
I'm using Python 3.6.5.


A:

You can use the <code>inspect</code> module to get the function arguments:
<code>from inspect import getfullargspec

def func(a, b, c):
    pass

print(getfullargspec(func).args)
</code>
Output:
<code>['a', 'b', 'c']
</code>

