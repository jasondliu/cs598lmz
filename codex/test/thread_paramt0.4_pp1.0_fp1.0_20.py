import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.collections as collections
import matplotlib.lines as lines
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import TextBox
from matplotlib.widgets import Cursor
from matplotlib.widgets import RectangleSelector
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import LassoSelector
from matplotlib.widgets import PolygonSelector
