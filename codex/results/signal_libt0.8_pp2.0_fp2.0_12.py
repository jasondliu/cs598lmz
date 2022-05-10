import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np
import time
import datetime

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import matplotlib.colors as colors

from . import param
from . import getdata
from . import getstocks
from . import getstocks2
from . import stockestimates
from . import StockEstimate
from . import colormaps
from . import colorutils
from . import pdbdata

def cmap_discretize(cmap, N):
    """Return a discrete colormap from the continuous colormap cmap.

        cmap: colormap instance, eg. cm.jet. 
        N: number of colors.

    Example
        x = resize(arange(100), (5,100))
        djet = cmap_discretize(cm.jet, 5)
        imshow(x, cmap=djet)
    """

    if type(cmap) == str:
       
