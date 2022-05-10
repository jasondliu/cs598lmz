import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def my_function(x):
    return x**2

c_func = FUNTYPE(my_function)

print(c_func(2))

#%%

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

#%%

import numpy as np
import mat
