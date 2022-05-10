import _struct

from pypy.interpreter.error import OperationError, oefmt
from pypy.interpreter.gateway import unwrap_spec
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.buffer import RWBuffer
from pypy.module._file.interp_file import W_File
from rpython.rlib import jit
from rpython.rlib.rarithmetic import r_longlong, r_uint, intmask
from rpython.rlib.objectmodel import specialize
from rpython.rlib.runicode import (
    str_decode_utf_8, str_encode_utf_8, unicode_encode_utf_8,
    unicode_decode_utf_8, unicode_encode_utf_16, unicode_decode_utf_16,
    unicode_encode_utf_32, unicode_decode_utf_32, unicode_encode_latin_1,
    unicode_decode_latin_1, unicode
