import weakref

import numpy
import six

from chainer.backends import cuda
from chainer.backends import intel64
from chainer import function
from chainer import function_node
from chainer import utils
from chainer.utils import argument
from chainer.utils import conv
from chainer.utils import type_check
from chainer import variable


if cuda.cudnn_enabled:
    cudnn = cuda.cudnn
    libcudnn = cuda.cuda.cudnn
    _cudnn_version = libcudnn.getVersion()
    _fwd_pref = libcudnn.CUDNN_CONVOLUTION_FWD_SPECIFY_WORKSPACE_LIMIT
    if _cudnn_version >= 3000:
        _bwd_filter_pref = \
            libcudnn.CUDNN_CONVOLUTION_BWD_FILTER_SPECIFY_WORKSPACE_LIMIT
        _bwd_data_pref = \
            libcudnn.CUDNN_CON
