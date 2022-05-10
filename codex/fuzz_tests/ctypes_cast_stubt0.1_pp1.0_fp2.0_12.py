import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import sys

# SOURCE LINE 5

from pypy.interpreter.error import OperationError
from pypy.interpreter.gateway import unwrap_spec
from pypy.interpreter.typedef import TypeDef
from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.buffer import SimpleView
from pypy.interpreter.buffer import Buffer
from pypy.interpreter.buffer import BufferView
from pypy.interpreter.buffer import ArrayBuffer
from pypy.interpreter.buffer import SubBuffer
from pypy.interpreter.buffer import BufferInterfaceNotSupported
from pypy.interpreter.buffer import BufferOverflow
from pypy.interpreter.buffer import BufferUnderflow
from pypy.interpreter.buffer import BufferFormat
from pypy.interpreter.buffer import BufferFormatError
from pypy.interpreter.buffer import BufferFormatOperations
from p
