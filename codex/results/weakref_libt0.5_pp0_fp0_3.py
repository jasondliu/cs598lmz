import weakref

import numpy as np

from . import util
from . import geometry
from . import mesh
from . import color
from . import gloo
from . import gl

log = logging.getLogger(__name__)


class BaseCamera(object):
    """Base class for cameras.

    Parameters
    ----------
    fov : float
        Field of view in degrees along the vertical direction.
    aspect : float
        Aspect ratio of the camera.
    near : float
        Distance to the near clipping plane.
    far : float
        Distance to the far clipping plane.
    """

    def __init__(self, fov=60, aspect=1, near=0.01, far=100):
        self.fov = fov
        self.aspect = aspect
        self.near = near
        self.far = far

    def set_range(self, aspect=None, fov=None, near=None, far=None):
        """Set the camera's range parameters.

        Parameters
        ----------
        aspect : float
            Aspect ratio of the camera.
