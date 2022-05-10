from types import FunctionType
list(FunctionType(lambda x: x+1, globals()).__code__.co_freevars)
 

# %%
f = lambda x: 10 * x + 3
f.__code__
f.__code__.co_code
dis.dis(f.__code__)

# %%
f = lambda x, y, z: 10 * x + 3
f.__code__
f.__code__.co_code
f.__code__.co_varnames
dis.dis(f.__code__)


# %%
0 + 10
3 + 20
6 + 30
9 + 40
12 + 50

# %%
from types import FunctionType
from dis import dis
list(FunctionType(lambda x: x + 1, globals()).__code__.co_freevars)

# %%
from types import FunctionType
from dis import dis
dis(FunctionType(lambda x: x + 1, globals()).__code__)

# %%
from types import FunctionType, CodeType
from dis import dis
dis(FunctionType(lambda x: x + 1
