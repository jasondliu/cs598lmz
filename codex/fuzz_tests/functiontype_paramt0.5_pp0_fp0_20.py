from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, 'new_name', f.func_defaults, f.func_closure))
</code>

