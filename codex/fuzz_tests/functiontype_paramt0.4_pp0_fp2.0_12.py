from types import FunctionType
list(FunctionType(lambda x: x+1, {}).__code__.co_varnames)

# 'x'
</code>

