import gc, weakref

import numpy as np

from . import _pyximport

_pyximport.install(setup_args={"include_dirs": np.get_include()})

from . import _cython_bbox
from . import _cython_nms

from . import _nms
from . import _nms_gpu
from . import _nms_cpu

from . import _box_utils
from . import _box_utils_gpu
from . import _box_utils_cpu

from . import _bbox
from . import _bbox_gpu
from . import _bbox_cpu

from . import _roi_align
from . import _roi_align_gpu
from . import _roi_align_cpu

from . import _roi_pool
from . import _roi_pool_gpu
from . import _roi_pool_cpu

from . import _crop_and_resize
from . import _crop_and_resize_gpu
from . import _crop_and_resize_cpu

from . import _de
