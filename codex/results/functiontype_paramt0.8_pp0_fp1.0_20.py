from types import FunctionType
list(FunctionType(lambda a: a, {'a': 1}).__globals__.keys())
['__builtins__', 'a']
</code>

