import weakref
import collections
import itertools

from . import _util
from . import _py2_xrange as _xrange
from . import _py2_xrange as range
from . import _py2_xrange as xrange
from . import _py2_xrange
from . import _py2_zip as zip
from ._py2_abc import ABCMeta

from . import _types
from . import _functools
from . import _operator
from . import _collections
from . import _weakref
from . import _itertools

from ._types import *  # Not a wildcard import
from ._functools import *  # Not a wildcard import
from ._operator import *  # Not a wildcard import
from ._collections import *  # Not a wildcard import
from ._weakref import *  # Not a wildcard import
from ._itertools import *  # Not a wildcard import

from ._types import _add_doc
from ._types import _check_methods
from ._types import _importer
from ._types import _is_sunder
from ._types
