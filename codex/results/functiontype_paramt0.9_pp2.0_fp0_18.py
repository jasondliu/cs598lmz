from types import FunctionType
list(FunctionType(c.func_code, {}).func_defaults)
FunctionType(c.func_code, {}).func_name
