import gc, weakref
import platform

from pypy.module._file import new_file,new_buffered_file
from pypy.module._file.interp_file import W_File
from pypy.interpreter.error import OperationError, operationerrfmt
from pypy.interpreter.gateway import ObjSpace
from pypy.interpreter.argument import Arguments
from pypy.interpreter.baseobjspace import Wrappable
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from rpython.rlib import rfile, rposix, rwin32
from rpython.rlib.rfile import create_popen_file, create_stdin, create_stdout, create_stderr, CConfigError
from rpython.rlib.rposix import get_fd_inheritable
from rpython.rlib.rwin32 import file_bom
from pypy.tool.udir import udir
import sys
import os

win32 = platform.system().lower() == 'windows'

win32
