from types import FunctionType
list(FunctionType(eval('lambda x: x'), globals())(k) for k in range(10))
</code>

