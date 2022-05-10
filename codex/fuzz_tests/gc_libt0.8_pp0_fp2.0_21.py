import gc, weakref
# from . import common
from . import porepy_tools as ptr
import discretize
import scipy.sparse as sps
import scipy
from . import imposition_tools
import discretize.utils
import mpl_toolkits.mplot3d.art3d
import pygmsh.built_in.geometry

NP = ptr.NP
_logger = ptr.logger(__name__)


class GridBucket(ptr.PorePyObject):
    """
    The grid bucket contains the information of a 2d or 3d grid.
    """
    def __init__(self, gb, physdims=None):
        self.physdims = physdims
        self.gb = gb
        self.dim_max = self.gb.dim_max()

    def __getitem__(self, *args, **kwargs):
        return self.gb.__getitem__(*args, **kwargs)

    def __iter__(self):
        return self.gb.__iter__()

    def __len__(
