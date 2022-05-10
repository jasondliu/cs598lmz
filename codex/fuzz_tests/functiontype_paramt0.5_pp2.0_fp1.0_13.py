from types import FunctionType
list(FunctionType(lambda: None, {}, 'foo').__code__.co_varnames)

# Output:
['foo']
</code>

