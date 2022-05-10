import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

import numpy as np
from numpy import pi
from numpy import sin
from numpy import cos

from scipy.integrate import quad

from wares.utils.sphere import sphere_inclined_conical


class SphericalLens(Function):
    """A spherical lens.

    Parameters
    ----------
    diameter : float, optional
        The diameter of the spherical lens.
    """
    def __init__(self, diameter=None):
        super(SphericalLens, self).__init__()
        self.diameter = diameter

    def __call__(self, x, y, z=0.0, wavelength=None):
        """Compute the complex amplitude of the optical field.

        Parameters
        ----------
        x : array-like
            The x-positions at which to compute the field.
        y : array-like
            The y-positions at which to compute the field.
        z : array-like, optional
            The z-positions at which to compute the field.

