import gc, weakref

import numpy, scipy, scipy.linalg
from numpy.linalg import lstsq as lstsq

from . import structure, util
from .util import *

from .structure import *
from .structure import __all__ as structure_exports

from ._linalg import *
from ._linalg import __all__ as linalg_exports
from ._linalg import _ExponentialMap, _LogarithmicMap
from ._linalg import _Adjoint, _Projection

from .differentiation import *
from .differentiation import __all__ as differentiation_exports

from . import lie_group_element as lie_group_element_module
from .lie_group_element import __all__ as lie_group_element_exports
from .lie_group_element import *

from . import lie_group as lie_group_module
from .lie_group import __all__ as lie_group_exports
from .lie_group import *

from . import optimization as optimization_module
from .optimization import __
