import ctypes
ctypes.cast(0, ctypes.py_object)

from llvmlite import ir
import llvmlite.binding as llvm
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()  # yes, even this one

from numpy import dtype

from numba.core import utils, cgutils, types, sigutils, typing
from numba.core.extending import intrinsic
from numba.core.compiler_lock import global_compiler_lock
from numba.core.ir_utils import (guard, find_callname,
                                rewrite_args, get_definition,
                                find_build_sequence, find_first_real_line,
                                get_mangled_name, get_name_var_table)
from numba.core.ir import (Assign, Const, Attribute, Global, Expr,
                           FreeVar, Block, Branch,
                           Phis, Del, Jump, Call,
                           SetItem, StaticGetItem, Load, Store,
                           static_cast
