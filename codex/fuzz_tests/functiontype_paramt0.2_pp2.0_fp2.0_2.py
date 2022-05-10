from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# TypeError: 'module' object is not callable
list(types.FunctionType(lambda x: x, globals(), "lambda"))
</code>

