import weakref

import numpy as np

from . import _pyximport
from . import _utils
from . import _utils_cy
from . import _utils_np
from . import _utils_np_cy
from . import _utils_np_cy_pyx
from . import _utils_pyx
from . import _utils_pyx_cy
from . import _utils_pyx_cy_np

_pyximport.install()

__all__ = [
    "utils",
    "utils_cy",
    "utils_np",
    "utils_np_cy",
    "utils_np_cy_pyx",
    "utils_pyx",
    "utils_pyx_cy",
    "utils_pyx_cy_np",
]


def _get_module_name(module):
    return module.__name__.rsplit(".", 1)[-1]


def _get_module_version(module):
    return module.__version__


def _get_module_version_info(module):
    return module.__version_
