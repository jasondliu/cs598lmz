import _struct
import ctypes
import ctypes.util
import errno
import fcntl
import os
import select
import socket
import struct
import sys
import time

from pypy.interpreter.error import OperationError
from pypy.interpreter.gateway import unwrap_spec
from pypy.interpreter.typedef import TypeDef
from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.typedef import interp_attrproperty
from pypy.interpreter.gateway import interp2app, ObjSpace, WrappedDefault
from pypy.rlib.rposix import get_errno, set_errno
from pypy.rlib import rgc
from pypy.rlib.unroll import unrolling_iterable
from pypy.rlib.rarithmetic import intmask, r_uint, r_ulonglong
from pypy.rlib.rstring import StringBuilder
from pypy.rlib import rthread
