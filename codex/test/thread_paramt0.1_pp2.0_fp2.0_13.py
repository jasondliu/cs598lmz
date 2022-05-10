import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.lines as lines
import matplotlib.collections as collections
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import matplotlib.gridspec as gridspec
import matplotlib.widgets as widgets
import matplotlib.text as text
import matplotlib.transforms as transforms
import matplotlib.ticker as ticker
import matplotlib.font_manager as font_manager
import matplotlib.image as image
import matplotlib.contour as contour
import matplotlib.contourf as contourf
import matplotlib.tri as tri
import matplotlib.delaunay as delaunay
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplot
