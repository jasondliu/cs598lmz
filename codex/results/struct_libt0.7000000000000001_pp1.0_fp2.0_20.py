import _struct

from rpython.rtyper.lltypesystem import rffi, lltype
from rpython.rtyper.lltypesystem.lloperation import llop
from rpython.rtyper.annlowlevel import llhelper
from rpython.rlib.rarithmetic import r_uint, intmask
from rpython.rlib.rawstorage import alloc_raw_storage
from rpython.rlib.debug import make_sure_not_resized
from rpython.rlib import jit

from pypy.interpreter.error import oefmt, wrap_oserror, OperationError
from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.gateway import interp2app, interpindirect2app
from pypy.interpreter.gateway import unwrap_spec
from pypy.interpreter.buffer import Buffer
from pypy.interpreter.argument import Arguments
from pypy.module.cpyext
