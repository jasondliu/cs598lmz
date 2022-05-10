import lzma
lzma.LZMAError
from   lzma import compress, decompress
from   io   import BytesIO
import numpy
from   datetime import datetime
from   datetime import timedelta

from   matplotlib.figure import Figure
from   matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.cm as cm
from   matplotlib.ticker import ScalarFormatter

from   .. import xarray_utils
from   .. import utils
from   .. import time_utils
from   .. import geo_utils
from   .. import geo_tools

from   . import logger
from   . import __version__
from   . import __git_version__


class NoData(Exception):
    pass


class Overlap(Exception):
    pass


class NoDataAtTime(Exception):
    pass


class NoDataAtStation(Exception):
    pass


class NoDataAtLatLon(Exception):
    pass


class NoDataAtStationAndTime(Exception):
    pass


class NoDataAtLatLonAndTime(
