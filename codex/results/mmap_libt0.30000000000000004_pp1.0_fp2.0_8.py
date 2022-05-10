import mmap
import os
import struct
import sys
import time

from . import _common
from . import _constants
from . import _exceptions
from . import _util
from . import _util_py2
from . import _util_py3
from . import _util_py33
from . import _util_py34
from . import _util_py35
from . import _util_py36
from . import _util_py37
from . import _util_py38
from . import _util_py39

if sys.version_info >= (3, 3):
    from . import _util_py33

if sys.version_info >= (3, 4):
    from . import _util_py34

if sys.version_info >= (3, 5):
    from . import _util_py35

if sys.version_info >= (3, 6):
    from . import _util_py36

if sys.version_info >= (3, 7):
    from . import _util_py37

if sys.version_info >= (3, 8):

