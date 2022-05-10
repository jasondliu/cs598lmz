import ctypes
ctypes.cast(0, ctypes.c_void_p)

#%% md

## Usage

#%% codecell
try:
    from .timer import Timer
except (ModuleNotFoundError, ImportError):
    class Timer:
        def __init__(self, ts, dt):
            self.ts = ts
            self.dt = dt
            
        def __call__(self, f):
            return f

#%% codecell
with Timer(ts, dt):
    c = a + b  #

a.shape
#%% codecell
c.shape
#%% codecell
c = a + b
#%% codecell
c.sum()
c.nbytes
#%% codecell
d = a + b

#%% codecell
d.sum()
#%% codecell
e = a + b
#%% codecell
e.sum()
#%% codecell
f = a + b
#%% codecell
f.sum()

#%% codecell
# Dict of all vars
cur_locals = locals()

#%%
