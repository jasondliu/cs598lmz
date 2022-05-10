import ctypes
ctypes.cdll.LoadLibrary('libX11.so')
ctypes.cdll.LoadLibrary('libXext.so')

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.widgets import RectangleSelector
from matplotlib import gridspec

from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import Cutout2D
from astropy.nddata.utils import Cutout2DShapeError
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import Angle
from astropy.visualization import ZScaleInterval, ImageNormalize
from astropy.visualization.mpl_normalize import ImageNormalize, simple_norm
from astropy.table import Table, Column

from scipy import ndimage
from scipy.ndimage.measurements import center_of_mass
from scipy.
