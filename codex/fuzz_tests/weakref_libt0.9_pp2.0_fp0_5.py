import weakref, itertools
from pkg_resources import iter_entry_points

try:
    from nipy.neurospin.spatial_models import hroi
    from nipy.neurospin.spatial_models import LabeledSpheres 
except ImportError:
    hroi = None
try:
    from matplotlib.nxutils import points_inside_poly
    from matplotlib import collections  as mpcollections
    from matplotlib import path as mppath
except ImportError:
    points_inside_poly = None
import pyhrf
from pyhrf.graph import graph_from_lattice, compute_local_minima
from pyhrf.ndarray import MRI3Daxes
from pyhrf.stats import tmax, pvalue
from pyhrf.tools import format_data_shape

__docformat__ = 'restructuredtext'

pyhrf.verbose.set_verbosity(2)

# fixme : voxel size is not taken into account in smoothing ...
# -> need to set voxel size in
