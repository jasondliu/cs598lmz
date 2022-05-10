import gc, weakref
from itertools import chain, count
from collections import defaultdict

from . import _util

from . import _matrix
from . import _vector
from . import _matrix_composite
from . import _vector_composite
from . import _matrix_slicing
from . import _vector_slicing
from . import _matrix_boolean
from . import _vector_boolean
from . import _matrix_numeric
from . import _vector_numeric
from . import _matrix_numpy
from . import _vector_numpy

from . import _matrix_composite_numpy
from . import _vector_composite_numpy
from . import _matrix_slicing_numpy
from . import _vector_slicing_numpy
from . import _matrix_boolean_numpy
from . import _vector_boolean_numpy
from . import _matrix_numeric_numpy
from . import _vector_numeric_numpy

from . import _matrix_composite_scip
