from types import FunctionType
list(FunctionType(lambda x: x+1, {}, None, None, None).__code__.co_varnames)

# co_varnames
# list(FunctionType(lambda x: x+1, {}, None, None, None).__code__.co_varnames)
# list(FunctionType(lambda x: x+1, {}, None, None, None).__code__.co_varnames)
# 'x'

# code object
# FunctionType(lambda x: x+1, {}, None, None, None).__code__
# <code object <lambda> at 0x00000214C70CBDC0, file "", line 1>

# co_name
# FunctionType(lambda x: x+1, {}, None, None, None).__code__.co_name
# '<lambda>'

# code object
# FunctionType(lambda x: x+1, {}, None, None, None).__code__
# <code object <lambda> at 0x00000214C70CBDC0, file "", line 1>

# co_argcount
