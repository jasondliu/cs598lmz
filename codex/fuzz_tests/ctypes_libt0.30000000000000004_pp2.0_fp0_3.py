import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.path as path
from matplotlib.widgets import Button
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import TextBox
from matplotlib.widgets import RectangleSelector
from matplotlib.widgets import Cursor
from matplotlib.widgets import Lasso
from matplotlib.widgets import PolygonSelector
from matplotlib.widgets import MultiCursor
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import EllipseSelector
from matplotlib.widgets import RectangleSelector
from matplotlib.widgets import LassoSelector
from matplotlib.widgets import
