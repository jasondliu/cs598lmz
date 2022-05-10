from types import FunctionType
list(FunctionType(f.func_code, f.func_globals).func_code.co_varnames)

# ['a', 'b', 'c', 'd', 'e']
</code>

