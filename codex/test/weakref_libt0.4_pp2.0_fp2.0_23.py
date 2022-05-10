import weakref

import numpy as np
from scipy.spatial import cKDTree

from .. import util
from .. import groupers
from .. import filters
from .. import cbook
from .. import docstring
from .. import rcParams
from .. import _api
from .. import artist
from ..artist import Artist, allow_rasterization
from ..cbook import iterable, is_string_like, is_numlike, maxdict
from ..path import Path
from ..transforms import Bbox, IdentityTransform, Transform, Affine2D
from ..transforms import blended_transform_factory
from ..transforms import ScaledTranslation, Affine2DBase
from ..transforms import BboxTransformTo, TransformedBbox
from ..transforms import TransformedPath
from ..transforms import Interval, Value, get_bbox_transform
from ..patch import Patch
from ..collections import Collection, RegularPolyCollection
from ..collections import PathCollection, LineCollection
from ..collections import PolyCollection
from ..collections import QuadMesh
from ..collections import EventCollection
from ..collections import Barbs
