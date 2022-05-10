import gc, weakref
from pypy.interpreter.error import OperationError
from pypy.interpreter.gateway import unwrap_spec
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.buffer import RWBuffer
from pypy.interpreter.typedef import interp_attrproperty
from pypy.interpreter.gateway import interp2app
from rpython.rlib import rgc
from rpython.rlib.objectmodel import instantiate
from rpython.rlib.rarithmetic import ovfcheck
from rpython.rlib.rweakref import RWeakValueDictionary
from rpython.rlib.rstring import StringBuilder
from rpython.rlib.rstruct.runpack import runpack
from rpython.rlib.rstruct.nativefmttable import native_is_bigendian
from rpython.rlib.rstruct.error import StructError
from rpython.rlib.rstruct import standardfmttable

