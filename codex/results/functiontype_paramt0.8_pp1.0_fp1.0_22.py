from types import FunctionType
list(FunctionType(code, globals={}) for code in codes)
</code>

