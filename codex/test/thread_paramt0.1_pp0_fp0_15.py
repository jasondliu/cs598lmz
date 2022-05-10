import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

from matplotlib.widgets import Button

from matplotlib.collections import PatchCollection

from matplotlib.patches import Rectangle

from matplotlib.widgets import Slider

from matplotlib.widgets import RadioButtons

from matplotlib.widgets import CheckButtons

from matplotlib.widgets import TextBox

from matplotlib.widgets import Cursor

from matplotlib.widgets import MultiCursor

from matplotlib.widgets import SpanSelector

from matplotlib.widgets import LassoSelector

from matplotlib.widgets import RectangleSelector

from matplotlib.widgets import EllipseSelector

from matplotlib.widgets import PolygonSelector

from matplotlib.widgets import AxesWidget

from matplotlib.widgets import Check
