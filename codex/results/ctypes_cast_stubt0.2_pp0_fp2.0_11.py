import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 2

from rpython.rlib.rarithmetic import intmask
from rpython.rlib.objectmodel import specialize
from rpython.rlib.objectmodel import we_are_translated
from rpython.rlib.debug import make_sure_not_resized
from rpython.rlib import jit
from rpython.rlib.jit import dont_look_inside
from rpython.rlib.unroll import unrolling_iterable
from rpython.rlib import rstring
from rpython.rlib.rstring import StringBuilder
from rpython.rlib.rbigint import rbigint
from rpython.rlib.rbigint import rbigint_fromint
from rpython.rlib.rbigint import rbigint_fromrarith_int
from rpython.rlib.rbigint import rbigint_fromfloat
from rpython.rlib.rbigint import rbigint_fromascii
from rpython.rlib.rbigint import rbigint_fromdecimalstr
from
