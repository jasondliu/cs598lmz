import weakref

from .. import _core
from .._core import UFuncType
from ..lib import stride_tricks
from ..lib import index_tricks
from ..lib import shape_base
from ..lib import arraypad
from ..lib import function_base
from ..lib import histograms
from ..lib import twodim_base
from ..lib import utils
from ..lib.stride_tricks import broadcast_to
from ..lib.stride_tricks import broadcast_arrays
from ..lib.index_tricks import AxisConcatenator
from ..lib.shape_base import atleast_1d
from ..lib.shape_base import atleast_2d
from ..lib.shape_base import vstack
from ..lib.shape_base import hstack
from ..lib.arraypad import _validate_lengths
from ..lib.function_base import average
from ..lib.twodim_base import diag
from ..lib.twodim_base import diagflat
from ..lib.twodim_base import eye
from ..lib.twodim_base import fliplr
