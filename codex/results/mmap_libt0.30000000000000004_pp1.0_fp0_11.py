import mmap
import os
import sys
import time
import traceback

import numpy as np

from . import _dynet as dy
from . import _dynet_config as dycfg
from . import _dynet_expr as dyexpr
from . import _dynet_model as dymod
from . import _dynet_param as dyparam
from . import _dynet_utils as dyutils

# ------------------------------------------------------------------------------
# Dynet Exceptions.
# ------------------------------------------------------------------------------


class DynetError(Exception):
    """Base class for exceptions in this module."""
    pass


class DynetInitializationError(DynetError):
    """Exception raised for errors in the initialization of Dynet.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class DynetModelError(DynetError):
    """Exception raised for errors in the Dynet model.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message =
