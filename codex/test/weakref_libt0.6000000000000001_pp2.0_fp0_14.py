import weakref

import numpy as np
import simpy
from scipy.spatial import cKDTree

from ..utils import memoize_method
from ..utils.geometry import point_to_segment_distance
from ..utils.numba import jit
from ..utils.random import get_rng
from ..utils.simpy import PriorityResource
from ..utils.timing import time_ns

from . import events
from . import kinematics
from . import obstacles
from . import obstacles_2d
from . import obstacles_3d
from . import topology
from . import topology_2d
from . import topology_3d
from . import traffic_lights
from . import vehicles
from . import vehicles_2d
from . import vehicles_3d

from .events import EventSink, EventSource
from .topology import Topology
from .topology_2d import Topology2D
from .topology_3d import Topology3D
from .vehicles import Vehicle
