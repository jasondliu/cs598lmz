from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults).func_closure)
</code>

