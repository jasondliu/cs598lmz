import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import sys
import os
import time
import threading
import traceback
import warnings
import weakref

# SOURCE LINE 11

from pypy.interpreter.error import OperationError, oefmt
from pypy.interpreter.gateway import unwrap_spec
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.buffer import Buffer
from pypy.interpreter.executioncontext import ExecutionContext
from pypy.interpreter.pycode import PyCode
from pypy.interpreter.pyframe import PyFrame
from pypy.interpreter.pyopcode import ExitFrame
from pypy.interpreter.signature import Signature
from pypy.interpreter.typedef import interp_attrproperty
from pypy.interpreter.argument import Arguments
from pypy.interpreter.module import
