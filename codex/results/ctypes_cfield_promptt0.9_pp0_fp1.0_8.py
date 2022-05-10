import ctypes
# Test ctypes.CField subclassing.

from ctypes import *

# Now try a little more complicated version.
class X(Structure):
    _fields_ = [('foo', c_int),
                ('bar', c_short),
                ('batz', c_short),
                ]

class Y(X):
    _fields_ = [('foo', c_long),
                ('fnord', c_double),
                ]

print sizeof(X), X().bar.offset, X().batz.offset
print sizeof(Y), Y().bar.offset, Y().batz.offset, Y().fnord.offset

class Z(Structure):
    _fields_ = [('foo', c_long),
                ('fnord', c_double),
                ('batz', Y),
                ]

print sizeof(Z), Z().batz.batz.offset, Z().batz.fnord.offset

print Z.batz.batz.offset == Z().batz.batz.offset
print Z.batz.fnord.offset == Z().batz.fnord.offset


