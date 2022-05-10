import mmap
import os
import shutil
import struct
import sys
import tempfile
from subprocess import Popen, PIPE
from textwrap import dedent

import numpy as np
import pytest

from numba import njit, prange, types
from numba.core import config, utils, ir_utils
from numba.core.compiler import compile_isolated, Flags, CompilerBase
from numba.core.errors import (TypingError, UnsupportedError,
                               LoweringError, NumbaDeprecationWarning,
                               NumbaWarning)
from numba.core.typing.templates import (ConcreteTemplate, AbstractTemplate,
                                         signature)
from numba.tests.support import (TestCase, captured_stdout, override_config,
                                 CompilationCache, MemoryLeakMixin,
                                 MemoryLeakMixinBase, tag, temp_directory,
                                 unittest)
from numba.tests.support import captured_stdout, override_config, temp_directory
from numba.core.compiler_lock import global_comp
