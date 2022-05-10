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
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import TextBox
from matplotlib.widgets import Cursor
from matplotlib.widgets import RectangleSelector
from matplotlib.widgets import LassoSelector
from matplotlib.widgets import MultiCursor
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import PolygonSelector
from matplotlib.widgets import EllipseSelector
from matplotlib.
