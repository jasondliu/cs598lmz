import gc, weakref

from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.gateway import interp2app, unwrap_spec, WrappedDefault
from pypy.interpreter.error import OperationError, oefmt
from rpython.rlib.objectmodel import specialize
from rpython.rlib import rarithmetic, jit
from rpython.rlib import rgc
from rpython.rlib.debug import ll_assert
from rpython.rlib.objectmodel import compute_unique_id
from rpython.rtyper.lltypesystem import lltype, llmemory, rffi
from rpython.rtyper.annlowlevel import llhelper
from rpython.rlib.objectmodel import instantiate
from rpython.rlib.rarithmetic import intmask
from rpython.rlib.rweaklist import RWeakListMixin
from rpython.rlib.rweakref import WeakRef
from rpython.rlib import rweakref, rgc
from rpython.rlib.jit import we_are_jitted
from r
