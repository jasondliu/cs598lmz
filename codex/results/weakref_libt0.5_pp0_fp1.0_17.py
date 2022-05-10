import weakref

import numpy as np

from . import _backend
from .. import units as u
from .. import time as time
from ..utils import isiterable, is_time_quantity, is_scalar
from ..time import Time, TimeDelta
from ..utils.compat.odict import OrderedDict
from ..utils.decorators import deprecated_renamed_argument
from ..utils.exceptions import AstropyWarning
from ..utils.console import color_print
from ..utils.data import get_pkg_data_contents
from ..utils.exceptions import AstropyUserWarning
from ..utils.xml.writer import xml_escape
from ..table import Table, Column, QTable
from ..table.pprint import table_formatter
from ..table.column import BaseColumn
from ..table.numpy_table import NumpyTableMixin
from ..coordinates import BaseCoordinateFrame
from ..coordinates.representation import CartesianRepresentation, SphericalRepresentation
from ..coordinates.builtin_frames import ICRS, FK4, FK5, Galactic, AltAz, GCRS, HC
