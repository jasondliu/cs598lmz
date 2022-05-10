import weakref

import numpy as np

from . import _base
from . import _util
from . import _data_obj


class _Data(_base.Data):
    """
    Base class for all data types.

    This class is not intended to be used directly.
    """

