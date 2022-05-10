from types import FunctionType
list(FunctionType(code, globals())(*args, **kwargs))
</code>

