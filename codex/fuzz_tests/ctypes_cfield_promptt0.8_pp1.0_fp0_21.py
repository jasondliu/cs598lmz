import ctypes
# Test ctypes.CField object
import _ctypes_test

FOOBAR = 777

class X(ctypes.Structure):
    _fields_ = [("foobar", ctypes.CField(ctypes.c_double, FOOBAR))]

class Y(ctypes.Structure):
    _fields_ = [("bar", ctypes.c_long),
                ("foobar", ctypes.CField(ctypes.c_double, FOOBAR))]

class Z(ctypes.Structure):
    _fields_ = [("foobar", ctypes.CField(ctypes.c_double, FOOBAR)),
                ("bar", ctypes.c_long)]

# XXX Allocates memory for _ctypes_test.X, _ctypes_test.Y, _ctypes_test.Z
# structures, but these structures are not properly initialized.  This
# causes the following ctypes test to crash on some platforms, e.g.
# FreeBSD x86.  For more details, see:
# http://bugs.python.org/issue6349
#
# Test
