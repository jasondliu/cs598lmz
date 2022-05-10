import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from matplotlib.widgets import TextBox
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import Cursor
from matplotlib.widgets import RectangleSelector
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import LassoSelector
from matplotlib.widgets import EllipseSelector
from matplotlib.widgets import PolygonSelector
from matplotlib.widgets import MultiCursor

from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
from matplotlib.patches import Polygon
from matplotlib.patches import FancyArrow
from matplotlib
