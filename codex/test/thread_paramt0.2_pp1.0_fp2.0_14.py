import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Circle
from matplotlib.patches import Wedge
from matplotlib.patches import Polygon
from matplotlib.patches import Ellipse
from matplotlib.patches import Arc
from matplotlib.patches import FancyArrow
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import ConnectionPatch
from matplotlib.patches import Arrow
from matplotlib.patches import ArrowStyle
from matplotlib.patches import BoxStyle
from matplotlib.patches import FancyBboxPatch
