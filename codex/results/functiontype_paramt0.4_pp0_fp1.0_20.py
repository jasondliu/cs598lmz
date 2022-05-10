from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

#%%
import inspect
inspect.getsource(f)

#%%
inspect.getclosurevars(f)

#%%
inspect.getclosurevars(f).nonlocals

#%%
import dis
dis.dis(f)

#%%
f.__code__.co_freevars

#%%
f.__closure__

#%%
f.__closure__[0].cell_contents

#%%
f.__closure__[1].cell_contents

#%%
f.__closure__[2].cell_contents

#%%
f.__closure__[3].cell_contents

#%%
f.__closure__[4].cell_contents

#%%
f.__closure__[5].cell_contents

#%%
f.__closure__[6].cell_contents

#%%
f.__closure__[7].cell
