import types
types.ClassType = type

from . import _faiss
from . import _swigfaiss
from .index_factory import Index
from .index_factory import make_index
from .index_factory import default_index_parameters, default_index_parameters_idmap
from .index_factory import default_index_parameters_sdc
from .index_factory import default_index_parameters_clustering
from .index_factory import default_index_parameters_pq
from .index_factory import default_index_parameters_ivf
from .index_factory import default_index_parameters_gpu
from .index_factory import default_index_parameters_cpu
from .index_factory import default_index_parameters_hnsw
from .index_factory import default_index_parameters_flat
from .index_factory import default_index_parameters_scalar_quantizer
from .index_factory import default_index_parameters_permutation
from .index_factory import default_index_parameters_composite
