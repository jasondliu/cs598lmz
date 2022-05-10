import ctypes
ctypes.cdll.LoadLibrary("libtrimesh.so")

from . import voxel
from . import affine
from . import transform
from . import arpoisson
from . import io
from . import ray
from . import clustering
from . import remeshing
from . import interpolate
from . import sample
from . import smoothing
from . import repair
from . import graph
from . import util
from . import geometry
from . import visual
from . import scene
from . import path

import logging
logger = logging.getLogger('trimesh')

# set the module level logger to the numpy logger
logger.setLevel(logging.WARNING)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# set scipy warning level to only raise on errors
sp_logger = logging.getLog
