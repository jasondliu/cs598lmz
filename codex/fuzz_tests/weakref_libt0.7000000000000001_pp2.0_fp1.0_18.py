import weakref

import numpy as np

import astropy.units as u

from . import constants
from . import orbits
from . import wcs
from . import distance
from . import coordinates
from .utils.wcs import WCS, WCS_INVALID

from .wcs.utils import pixel_to_skycoord


__all__ = ['Map', 'MapBase', 'MapCoord', 'MapCoord_WA', 'MapCoord_DS9',
           'MapCoord_Nominal', 'MapCoord_INVALID']

class MapCoord_INVALID(object):
    pass

class MapCoord(object):

    def __init__(self, name, description, unit, coord,
                 default_origin='center', default_corner='lower'):

        self.name = name
        self.unit = unit
        self.description = description
        self.coord = coord
        self.default_origin = default_origin
        self.default_corner = default_corner

    def __repr__(self):
        return "<{:s}: {:s}
