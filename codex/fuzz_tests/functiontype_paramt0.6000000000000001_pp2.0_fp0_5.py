from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, name=f.func_name,
    argdefs=f.func_defaults, closure=f.func_closure))
</code>

