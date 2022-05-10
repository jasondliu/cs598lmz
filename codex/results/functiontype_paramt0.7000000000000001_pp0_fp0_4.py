from types import FunctionType
list(FunctionType(f.func_code, globals())() for f in (f1,f2))
</code>

