from types import FunctionType
list(FunctionType(lambda: 1, globals(), 'lambda', (), None, None).__code__.co_freevars)

# Output:
['__builtins__']
</code>

