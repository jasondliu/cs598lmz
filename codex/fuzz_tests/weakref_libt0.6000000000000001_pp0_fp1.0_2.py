import weakref

from . import util
from . import graph
from . import _sparsetools
from . import _sparsetools as ss

from . import _csparsetools
from . import _csparsetools as cs

from .sputils import upcast_char, upcast, getdtype, isscalarlike, isshape

from ._compressed import _cs_matrix
from ._data import _data_matrix, _minmax_mixin
from ._index import _index_shared_mixin, _cs_index
from ._slicing import _csr_to_bsr, _csr_matrix_compressed_indices
from ._sort import _csr_matrix_sort_indices
from ._sparsetools import csr_tocsc, csr_count_blocks, \
        csr_sample_values, csr_swap_indices, csr_tobsr
from . import _csparsetools
from .sputils import get_index_dtype, isintlike
from . import _csparsetools
