from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# FunctionType(lambda: None, {})
# <function <lambda> at 0x7f5d7f0b5f28>
# FunctionType(lambda: None, {}).__code__
# <code object <lambda> at 0x7f5d7f0b5e50, file "<stdin>", line 1>
# FunctionType(lambda: None, {}).__code__.co_varnames
# ()

# FunctionType(lambda x: None, {})
# <function <lambda> at 0x7f5d7f0b5f28>
# FunctionType(lambda x: None, {}).__code__
# <code object <lambda> at 0x7f5d7f0b5e50, file "<stdin>", line 1>
# FunctionType(lambda x: None, {}).__code__.co_varnames
# ('x',)

# FunctionType(lambda x, y, z: None, {})
# <function <lambda> at 0x
