import ctypes
ctypes.cast(0, ctypes.py_object)

#This is a workaround for a bug in the Python interpreter:
#http://bugs.python.org/issue15881#msg170215

import sys
if sys.version_info[0] == 2:
    import thread
else:
    import _thread as thread

import time

import numpy as np

from . import _pysynphot as S
from . import spectrum
from . import observationmode
from . import observation
from . import units
from . import exceptions
from . import refs
from . import observationmode
from . import observation
from . import spectra
from . import reddening
from . import units
from . import exceptions
from . import refs
from . import observationmode
from . import observation
from . import spectra
from . import reddening
from . import units
from . import exceptions
from . import refs
from . import observationmode
from . import observation
from . import spectra
from . import reddening
from . import units
from . import exceptions
from . import refs
from . import observationmode
from .
