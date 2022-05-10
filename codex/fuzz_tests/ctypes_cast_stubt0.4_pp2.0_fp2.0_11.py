import ctypes
ctypes.cast(id(0), ctypes.py_object).value

# PyPy
import __pypy__
__pypy__.internal_repr((1,))

# Jython
import org.python.core.PyStringMap
org.python.core.PyStringMap.toString()

# IronPython
import clr
clr.GetClrType(type(0))

# Stackless
import stackless
stackless.current.set_atomic(True)

# MicroPython
import uctypes
uctypes.addressof(0)

# Cython
import cython
cython.inline('a + b')

# Nuitka
import nuitka
nuitka.build.create_exe('')

# Shedskin
import shedskin
shedskin.inline('a + b')

# Numba
import numba
numba.jit(nopython=True)(lambda x: x + 1)

# Pyston
import pyston
pyston.run_string('print("Hello, World!")')

# P
