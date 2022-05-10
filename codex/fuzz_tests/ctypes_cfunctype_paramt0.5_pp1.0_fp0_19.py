import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
</code>
This is how I am trying to call the function:
<code>import numpy as np
import ctypes

# Function definition
def f(x):
    return 2*x

# Function definition in C
c_f = FUNTYPE(f)

# Input array
x = np.linspace(0, 1, 5)

# Array to hold results
y = np.zeros(5)

# Call function in C
c_f(x, y)
</code>
The error I get is:
<code>TypeError: in method 'f', argument 2 of type 'double *'
</code>
How can I make this work?


A:

You can use <code>numpy.fromiter</code> to convert the output to a numpy array:
<code>import numpy as np
import ctypes

# Function definition
def f(x):
    return 2*x

# Function definition in C
c_f = FUNTYPE(f)

# Input array

