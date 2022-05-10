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
