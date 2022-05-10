import gc, weakref

import matplotlib
import matplotlib.cbook as cbook
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import matplotlib.ticker as ticker
import matplotlib.cbook as cbook
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.artist as artist
import matplotlib.axis as maxis
import matplotlib.mlab as mlab
import matplotlib.numerix as nx
import matplotlib.numerix.ma as ma
from matplotlib.font_manager import FontProperties
from matplotlib.numerix.npyma import masked_equal, masked_less



def xmgrace_colormap(nc, fg_c, bg_c, mid_c):
    r, g, b = fg_c
    r fg_fg = r / 255.0
    fg_fg g = g / 255.0
    fg_fg b = b / 255.0
    r,
