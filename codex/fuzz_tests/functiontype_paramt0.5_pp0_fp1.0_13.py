from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda", (lambda x: x,), None).__code__.co_varnames)

# Output:
# ['x']
</code>

