from types import FunctionType
list(FunctionType(lambda x: x**2, globals())(i) for i in range(5))
[0, 1, 4, 9, 16]
</code>

