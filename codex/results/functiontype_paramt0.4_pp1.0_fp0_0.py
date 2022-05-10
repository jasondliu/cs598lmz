from types import FunctionType
list(FunctionType(f.__code__, globals(), 'my_func')())

#%%
def f(x):
    return x + 1

f_new = FunctionType(f.__code__, globals(), 'f_new', (), f.__defaults__)
f_new(2)

#%%
import inspect
def g(x):
    return x + 1

g_new = FunctionType(g.__code__, globals(), 'g_new', (1,), g.__defaults__)
g_new()

#%%
def h(x):
    return x + 1

h_new = FunctionType(h.__code__, globals(), 'h_new', (1,), (2,))
h_new()

#%%
def i(x):
    return x + 1

i_new = FunctionType(i.__code__, globals(), 'i_new', (1,), (2,))
inspect.getargspec(i_new)

#%%
def j(x):
    return x + 1

