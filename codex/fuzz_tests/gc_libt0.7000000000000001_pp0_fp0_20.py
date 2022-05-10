import gc, weakref
from pymel.internal.pmcmds import *
from pymel.internal.pmutil import getStringArgument
from pymel.internal.pmutil import isIterable
from pymel.util.utilitytypes import Singleton
from pymel.util import getClassType
import pymel.internal.factories as _factories
from pymel.internal.factories import _factoriesUtils
from pymel.internal.factories import _factoriesUtils as _fu

_logger = logging.getLogger(__name__)

# Python 2.6 compatibility
try:
    from collections import OrderedDict as _orderedDict
except ImportError:
    from pymel.util.ordereddict import OrderedDict as _orderedDict

#===============================================================================
# Python 2.6 compatibility
#===============================================================================
try:
    unicode
except NameError:
    unicode = str

#===============================================================================
# Exceptions
#===============================================================================
class TimeoutError(Exception):
    pass

#===============================================================================
# Utilities

