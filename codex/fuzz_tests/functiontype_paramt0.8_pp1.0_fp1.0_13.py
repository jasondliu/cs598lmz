from types import FunctionType
list(FunctionType(b.__code__, globals())(2))
</code>

