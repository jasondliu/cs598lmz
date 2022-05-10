import gc, weakref
import os
import copy
import logging

from . import _support
from . import _imaging
from . import _imagingcms
from . import _imagingmath
from . import _imagingmorph
from . import _imagingft
from . import _imagingdraw
from . import _imagingtk
from . import _imagingmath
from . import _imagingcopy
from . import _imagingtk

# --------------------------------------------------------------------
# Registry

ID = _imaging.ID

# --------------------------------------------------------------------
# Image type stuff

from ._imaging import (
    DEFAULT_STRATEGY, FILTERED, BOX, NEAREST, BILINEAR, BICUBIC, HAMMING,
    BLACKMAN, MAX, MEDIAN, MIN, MODE, LANCZOS
)

try:
    from ._imaging import (
        AFFINE, TRANSLATE, ROTATE, QUAD, PERSPECTIVE,
    )
except ImportError:
    pass

try:
    from ._imaging import (
        LUT, MESH, PIL_DECODE_
