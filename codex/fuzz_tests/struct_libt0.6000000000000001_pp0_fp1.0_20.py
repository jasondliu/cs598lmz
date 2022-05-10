import _struct
from operator import itemgetter
from itertools import groupby

import numpy as np

from . import _util
from ._util import get_mpi_comm
from . import _distributed
from ._distributed import DistributedArray, DistributedArrayException, DistributedArrayMeta
from . import _distributed_array_base
from ._distributed_array_base import (
    DistributedArrayBase,
    DistributedArrayException,
    DistributedArrayMeta,
    _get_global_size,
    _get_global_shape,
    _get_global_ndim,
    _get_global_size_in_dims,
    _get_global_shape_in_dims,
    _get_local_size,
    _get_local_shape,
    _get_local_ndim,
    _get_local_size_in_dims,
    _get_local_shape_in_dims,
    _get_local_index,
    _get_local_index_in_dims,
    _get_local_to_global_
