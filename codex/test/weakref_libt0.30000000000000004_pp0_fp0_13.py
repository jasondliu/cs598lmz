import weakref

import numpy as np

from . import utils
from . import _backend
from . import _backend_utils
from . import _types
from . import _api_internal
from . import _ndarray_internal
from . import _internal
from . import _topi_compute
from . import _topi_schedule
from . import _topi_x86_cpu
from . import _topi_x86_gpu
from . import _topi_arm_cpu
from . import _topi_arm_gpu
from . import _topi_nn
from . import _topi_generic
from . import _topi_cuda
from . import _topi_ocl
from . import _topi_rocm
from . import _topi_nn_cpu
from . import _topi_nn_gpu
from . import _topi_nn_arm_cpu
from . import _topi_nn_arm_gpu
from . import _topi_nn_cuda
from . import _topi_nn_ocl
from . import _topi_nn_rocm
