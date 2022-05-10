from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
s.pack(1)

import _struct
_struct.pack('h', 1)

import _struct
_struct._clearcache()

import _struct
_struct.__doc__

import _struct
_struct.__file__

import _struct
_struct.__name__

import _struct
_struct.__package__

import _struct
_struct.__version__

import _struct
_struct._clearcache()
