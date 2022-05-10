from types import FunctionType
list(FunctionType('funcName', globals(), {}, None, None).__code__.co_varnames)
</code>

