import weakref

import numpy as np
import pandas as pd

from . import _utils
from . import _indexing
from . import _np_utils
from . import _vindex
from . import ops
from .pycompat import dask_array_type, dask_dataframe_type
