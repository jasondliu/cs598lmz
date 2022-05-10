import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

class PyCallback(object):
    def __init__(self, callback):
        self.callback = callback
        self.fun = FUNTYPE(self.callback)

    def __call__(self, x):
        return self.fun(x)

def callback(x):
    return x**2

cb = PyCallback(callback)

import numpy as np
x = np.linspace(0, 1, 1000)
y = cb(x)
</code>

