import mmap
from collections import defaultdict

from pyproj import Proj, transform
from shapely.geometry import Polygon, mapping, shape, Point
from shapely.ops import unary_union
from shapely.ops import cascaded_union
from rtree import index
from rtree.core import RTreeError
from rtree.index import Index

from .config import Config
from .utils import distance
from .utils import get_logger

logger = get_logger(__name__)


class Base(object):
    """
    Base class for all the other classes
    """
    def __init__(self, config):
        self.config = config
        self.index = Index()
        self.features = []
        self.reprojected_features = []
        self.reprojected_features_index = Index()
        self.reprojected_features_rtree = Index()
        self.reprojected_features_rtree_index = Index()
        self.rtree_index = Index()
        self.rtree_index_index = Index()
        self.
