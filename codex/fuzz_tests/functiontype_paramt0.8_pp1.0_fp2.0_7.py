from types import FunctionType
list(FunctionType(lambda: 3, globals(), "test")(5))
</code>

