from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), "add1")(i) for i in range(3))

# [1, 2, 3]
</code>

