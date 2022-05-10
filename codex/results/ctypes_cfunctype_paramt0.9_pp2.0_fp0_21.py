import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
</code>
To build the number of arguments list dynamically I use code like:
<code>argList = [ctypes.c_double for k in range(0, 21)]
FUNARG = tuple(argList)
</code>
With the above I can create any number of arguments I want in the function.  I can also create a function that always gets passed a list of arguments from Python and then picks out the number I want using code like:
<code>    inStr = "baz(s * 1000.0, a * 1000.0, c * 1000.0, d * 1000.0, e * 1000.0, f * 1000.0, g * 1000.0, h * 1000.0, i * 1000.0, j * 1000.0, k * 1000.0, l * 1000.0, m * 1000.0, n * 1000.0, o * 1000.0, p * 1000.0, q * 1000.0, r * 1000.0, t * 1000.0, u * 1000.0, v
