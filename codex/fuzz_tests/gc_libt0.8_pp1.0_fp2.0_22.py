import gc, weakref
from functools import partial
import struct
from collections import namedtuple
from pypy.objspace.std.listtype import W_ListStrategy, W_ListObject
from pypy.objspace.std.listobject import W_ListObject
from pypy.objspace.std.listobject import reversed_w
from pypy.interpreter.error import OperationError, operationerrfmt
from pypy.interpreter.buffer import Buffer
from pypy.interpreter.gateway import unwrap_spec
from rpython.rlib.rarithmetic import ovfcheck_float_to_int
from pypy.module.micronumpy.arrayimpl.buffer import RawArrayBuffer
from pypy.module.micronumpy.arrayimpl.memory import BaseW_NDimArray
from pypy.module.micronumpy import interp_dtype
from pypy.module.micronumpy.base import convert_to_array
from pypy.module.micronumpy.interp_numarray import get_dtype_cache
from rpython.rlib
