import ctypes
ctypes.cast(0, ctypes.py_object)

# now it should work...
import pyximport
pyximport.install()

import cython_example
print cython_example.primes(1000)
</code>

