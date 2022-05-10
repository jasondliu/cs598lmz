import weakref
from functools import partial
from itertools import chain
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    Union,
    cast,
)

import numpy as np

from pandas._libs import lib
from pandas._libs.interval import IntervalMixin
from pandas._libs.missing import isna
from pandas._libs.ops import na_arithmetic_op
from pandas._libs.ops_dispatch import dispatch_to_extension_op
from pandas._libs.reduction import (
    NaTGroupReduction,
    get_group_index,
    get_group_index_sorter,
    get_group_index_sorter_list,
    maybe_convert_ix,
    maybe_dispatch_ufunc_to_output_types,
)
from pandas._libs.sparse import BlockIndex, IntIndex
from pandas._libs
