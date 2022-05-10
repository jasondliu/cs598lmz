import mmap
import os

import numpy as np

from .. import utils
from .. import types
from .. import _constants as constants
from .. import _errors as errors
from . import _types as _ast_types
from . import _utils as _ast_utils
from . import _constants as _ast_constants
from . import _errors as _ast_errors
from . import _ir as _ast_ir

__all__ = ["Parser"]


class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, "rb")
        self.mmap = mmap.mmap(self.f.fileno(), 0, access=mmap.ACCESS_READ)
        self.start_offset = 0
        self.current_offset = 0
        self.end_offset = os.fstat(self.f.fileno())[6]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.mmap.
