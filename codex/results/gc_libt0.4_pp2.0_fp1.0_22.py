import gc, weakref

import numpy as np

from . import cuda_api, cuda_common
from .cuda_api import CUDA_API
from .cuda_common import cuda_available, cuda_error_check

from . import cuda_convnet2

from . import cuda_convnet2 as ccn
from .cuda_convnet2 import (
    convnet_convolution, convnet_convolution_backward, convnet_convolution_backward_weights,
    convnet_max_pool_locs, convnet_max_pool, convnet_max_pool_backward,
    convnet_local_response_normalization, convnet_local_response_normalization_backward)

from . import cuda_convnet2_kernels as ccn_k
from .cuda_convnet2_kernels import (
    convnet_convolution_kernel, convnet_convolution_backward_kernel, convnet_convolution_backward_weights_kernel,
    convnet_max_pool_locs_kernel, convnet_max
