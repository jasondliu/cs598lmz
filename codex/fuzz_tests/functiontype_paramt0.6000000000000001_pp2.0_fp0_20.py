from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# 5.9.3
from dis import dis
dis(FunctionType(lambda: None, {}))

# 5.9.4
from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_consts)

# 5.9.5
from types import FunctionType
from dis import dis
dis(FunctionType(lambda: None, {}))

# 5.9.6
from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_freevars)

# 5.9.7
from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_cellvars)

# 5.10.1
from types import FunctionType
FunctionType(lambda: None, {}).__code__.co_flags

# 5.10.2
from types import FunctionType
FunctionType(lambda: None, {}).__code__.co_flags & 0x20

# 5.10.3
from
