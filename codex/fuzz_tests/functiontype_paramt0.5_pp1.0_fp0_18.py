from types import FunctionType
list(FunctionType(f.func_code, f.func_globals))

# [1, 2, 3, 4]
</code>

