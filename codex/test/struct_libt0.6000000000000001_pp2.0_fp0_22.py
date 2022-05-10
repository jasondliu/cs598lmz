import _struct

from pypy.interpreter.error import OperationError, oefmt
from pypy.interpreter.gateway import unwrap_spec
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.buffer import RWBuffer
from pypy.module._file.interp_file import W_File
from rpython.rlib import jit
from rpython.rlib.rarithmetic import r_longlong, r_uint, intmask
from rpython.rlib.objectmodel import specialize
