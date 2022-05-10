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
import matplotlib.text as text
import matplotlib.font_manager as font_manager
import matplotlib.transforms as transforms
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import matplotlib.colorconverter as colorconverter
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
import matplotlib.spines as spines
import matplotlib.contour as contour
import matplotlib.contourf as contourf
import matplotlib.finance as finance
import matplotlib.dates as dates
import matplotlib.legend as legend
import matplotlib.image as image
import mat
