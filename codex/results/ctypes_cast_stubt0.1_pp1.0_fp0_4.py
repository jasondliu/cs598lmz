import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a hack to make sure that the C++ code is compiled.
import pyximport
pyximport.install()

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
import matplotlib.image as image
import matplotlib.backends.backend_pdf as pdf
import matplotlib.backends.backend_agg as agg
import matplotlib.backends.backend_svg as svg
import matplotlib.backends.backend
