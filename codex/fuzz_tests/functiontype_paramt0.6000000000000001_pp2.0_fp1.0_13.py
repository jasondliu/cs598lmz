from types import FunctionType
list(FunctionType(x.func_code, x.func_globals, x.func_name, x.func_defaults, x.func_closure))
# [1]
</code>

