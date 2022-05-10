import weakref
import logging
import math
import time

import numpy as np

from .base import Layer, Node
from . import helpers
from . import convolution
from . import pooling

from .. import backend
from .. import initializers
from .. import regularizers
from .. import constraints
from ..engine import LayerFromCallable
from ..utils.generic_utils import transpose_shape
from ..utils.generic_utils import slice_arrays
from ..utils.generic_utils import has_arg
from ..utils.generic_utils import to_list
from ..utils.generic_utils import object_list_uid
from ..utils.generic_utils import object_list_uid
from ..utils.generic_utils import unpack_singleton
from ..utils.generic_utils import unpack_x_y_sample_weight
from ..utils.generic_utils import unpack_sample_weight
from ..utils.generic_utils import unpack_x_y_sample_weight_3d
from ..utils.generic_utils import unpack_sample_weight_3d
from ..utils.generic_utils import unpack_x_y
