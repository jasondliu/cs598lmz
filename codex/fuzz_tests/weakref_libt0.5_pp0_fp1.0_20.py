import weakref

from . import _core
from . import _compat
from . import _util
from . import _weakref
from . import _metadata

from ._core import *
from ._compat import *
from ._util import *
from ._weakref import *
from ._metadata import *

# TODO:
# - add support for the following:
#   - __slots__
#   - __getattribute__
#   - __setattr__
#   - __delattr__
#   - __get__
#   - __set__
#   - __delete__
#   - __getitem__
#   - __setitem__
#   - __delitem__
#   - __len__
#   - __contains__
#   - __missing__
#   - __reversed__
#   - __iter__
#   - __next__
#   - __length_hint__
#   - __bool__
#   - __hash__
#   - __abs__
#   - __add__
#   - __sub__
#   - __mul
