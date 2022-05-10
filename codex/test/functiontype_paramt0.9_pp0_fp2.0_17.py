from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, f.func_closure) for f in [lambda a,b:c for a,b,c in []])
