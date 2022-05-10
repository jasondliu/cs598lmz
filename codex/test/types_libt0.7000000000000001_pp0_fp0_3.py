import types
types.ClassType = types.TypeType # fix for py2.2

try:
    import psyco
except ImportError:
    pass

import sre_constants
from sre_constants import *
from sre_parse import Pattern, SubPattern

from sre_compile import *
from sre_constants import *

try:
    from sre_parse import DEBUG
except ImportError:
    DEBUG = 0

# flags
SRE_FLAG_TEMPLATE = 128
SRE_FLAG_DEBUG = DEBUG

# --------------------------------------------------------------------
# public module interface

