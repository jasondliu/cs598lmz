from types import FunctionType
list(FunctionType(lambda:1,globals(),'func') for i in range(3))
</code>

