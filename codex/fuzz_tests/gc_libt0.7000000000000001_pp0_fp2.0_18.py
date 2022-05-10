import gc, weakref, sys, os
import tempfile, threading, time
from multiprocessing import Process, Queue

from llvm.core import *
from llvm.ee import *
from llvm.passes import *

from . import llvm_types
from . import function_passes
from . import utils
from . import types

log = logging.getLogger("pykit.compiler")

#===------------------------------------------------------------------===
# Compiler
#===------------------------------------------------------------------===

class Compiler(object):
    """
    The main interface to the Pykit compiler.

    The compiler compiles pykit functions to LLVM functions. This can be
    done either in process, or using a separate process.

    Compilation involves generating LLVM IR and linking it into a module.
    The module can optionally be optimized and JIT compiled.

    The main entry points are:

      compile_function(func)
        Compile and return a pykit function.

      compile_module(module)
        Compile a pykit module.

    The compiler uses a cache of compiled functions to avoid recompiling
    functions multiple times
