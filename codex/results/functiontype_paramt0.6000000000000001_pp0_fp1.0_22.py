from types import FunctionType
list(FunctionType(lambda: None, globals=dict(A=1, B=2)).__globals__.items())

# %%
from types import FunctionType
list(FunctionType(lambda: None, globals=dict(A=1, B=2)).__globals__.keys())

# %%
from types import FunctionType
list(FunctionType(lambda: None, globals=dict(A=1, B=2)).__globals__.values())

# %%
from types import FunctionType
FunctionType(lambda: None, globals=dict(A=1, B=2)).__globals__['B']

# %%
from types import FunctionType
FunctionType(lambda: None, globals=dict(A=1, B=2)).__globals__['A']

# %%
from types import FunctionType
FunctionType(lambda: None, globals=dict(A=1, B=2)).__globals__['C']

# %%
from types import FunctionType
FunctionType(lambda: None, globals=dict(A=1, B=2)).
