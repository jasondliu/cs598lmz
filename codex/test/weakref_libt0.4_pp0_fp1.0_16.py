import weakref

import numpy as np

from . import _utils
from . import _data_obj
from . import _data_iter_cpu
from . import io
from . import ndarray

if _utils.USE_MXNET_CORE:
    from mxnet.base import _LIB
    from mxnet.base import c_array, c_str, mx_uint, py_str
    from mxnet.base import DataBatch, DataIterHandle, NDArrayHandle
    from mxnet.base import mx_real_t
    from mxnet.base import check_call
    from mxnet.ndarray import NDArray


