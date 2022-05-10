import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from matplotlib.widgets import TextBox
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import Cursor

from matplotlib.collections import PatchCollection
from matplotlib.collections import LineCollection

from matplotlib.patches import Polygon
from matplotlib.patches import Circle
from matplotlib.patches import Wedge
from matplotlib.patches import Arc
from matplotlib.patches import Rectangle

from matplotlib.lines import Line2D

from matplotlib.path import Path

from matplotlib.transforms import Affine2D

from matplotlib.text import Text

from matplotlib.colors import LinearSegmentedCol
