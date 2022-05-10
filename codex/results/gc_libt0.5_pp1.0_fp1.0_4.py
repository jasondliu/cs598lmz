import gc, weakref

import numpy as np
from numpy import arange
from numpy.random import randn

from pandas import (Index, Series, DataFrame, Panel, Panel4D,
                    date_range, MultiIndex, Timestamp)
from pandas.core.api import (notnull, isnull, MultiIndex,
                             SparseDataFrame, SparseSeries)
import pandas.core.common as com
from pandas.core.common import isnull, notnull
from pandas.core.index import Index
from pandas.core.indexing import (IndexingError, _NDFrameIndexer,
                                  _maybe_droplevels, _non_reducing_slice)
from pandas.core.series import remove_na
from pandas.core.panel import Panel
from pandas.core.panel4d import Panel4D
from pandas.core.panelnd import PanelND, _extract_axes
from pandas.core.reshape import (concat, merge,
                                 get_dummies, wide_to_long)
from pandas.core.internals import
