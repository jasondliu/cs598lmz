from bz2 import BZ2Decompressor
BZ2Decompressor()  # pyflakes

from rpython.rlib import jit
from rpython.rlib.streamio import (open_file_as_stream, open_file_as_file,
                                   fopen, fdopen, Stream, fdopen_as_stream)
from rpython.rlib.rarithmetic import intmask
from rpython.rtyper.annlowlevel import llstr
from rpython.rtyper.lltypesystem import rffi, lltype
from rpython.translator.tool.cbuild import ExternalCompilationInfo
from rpython.translator.platform import platform

from pypy.interpreter.error import ( 
    OperationError, oefmt, PyException, exception_from_saved_errno)
from pypy.interpreter.typedef import TypeDef, GetSetProperty, interp_attrproperty
from pypy.interpreter.gateway import WrappedDefault, interp2app, unwrap_spec
from pypy.interpreter.baseobjspace import W_Root, ObjSpace, Wrappable,\

