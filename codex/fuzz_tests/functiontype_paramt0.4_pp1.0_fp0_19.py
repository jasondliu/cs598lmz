from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

#==============================================================================
# 
#==============================================================================

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-10, 10, 100)
y = f(x)

plt.plot(x, y)
plt.show()

#==============================================================================
# 
#==============================================================================

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-10, 10, 100)
y = f(x)

plt.plot(x, y)
plt.show()

#==============================================================================
# 
#==============================================================================

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-
