import gc, weakref, operator, functools
import sys, os
import warnings
from collections import defaultdict
from math import log
from time import time
from copy import copy, deepcopy

from pyx import *
from pyx import color
import numpy as np
from scipy.spatial import cKDTree
import shapely.geometry
from shapely.ops import cascaded_union
from shapely.geometry import Polygon, MultiPolygon, box
from shapely.geometry import LineString, MultiLineString
from shapely.geometry import Point, MultiPoint
from shapely.geometry import LinearRing, GeometryCollection
from shapely import affinity
from descartes.patch import PolygonPatch
from descartes.patch import PolygonPatch, LinePatch

from . import utils, geom, obj3d, path, path3d, shape
from . import units, settings
from .units import MM, INCH, default_units
from .utils import isiterable
from .cameras import camera
from .cameras import perspective, orthographic
from .cameras import camera3d,
