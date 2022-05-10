from types import FunctionType
list(FunctionType(lambda: 1, {}, 'lambda', (), None).__code__.co_freevars)

# Output:
# ['__builtins__']
</code>

