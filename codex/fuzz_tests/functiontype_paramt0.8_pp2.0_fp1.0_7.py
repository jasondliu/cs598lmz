from types import FunctionType
list(FunctionType(FunctionType(a.func_code, a.func_globals, "b", a.func_defaults, a.func_closure), {})())
</code>

