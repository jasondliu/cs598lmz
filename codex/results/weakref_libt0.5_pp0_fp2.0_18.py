import weakref

import numpy as np

from . import _base
from . import _interpolate
from . import _spline
from . import _polynomial
from . import _bspline
from . import _pchip
from . import _akima
from . import _fitpack
from . import _ppoly
from . import _dfitpack
from . import _ndimage
from . import _fitpack2


class _Interpolator1D(object):
    """
    Abstract base class for 1-dimensional interpolating classes.
    """

    def _call(self, x_new):
        """
        Overload this method in derived classes.

        Parameters
        ----------
        x_new : array_like
            New x-coordinates at which to interpolate.

        Returns
        -------
        y_new : array_like
            Interpolated values. Shape is determined by replacing
            the interpolation axis in the original array with the shape of
            `x_new`.
        """
        raise NotImplementedError

    def _call_linear(self, x_new):

