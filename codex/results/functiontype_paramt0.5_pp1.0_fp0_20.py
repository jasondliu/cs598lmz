from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, 'f', f.func_defaults, f.func_closure))
# [1, 2, 3]
</code>

