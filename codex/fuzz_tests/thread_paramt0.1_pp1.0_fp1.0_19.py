import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from matplotlib.patches import Polygon
from matplotlib.patches import Wedge
from matplotlib.patches import Arc
from matplotlib.patches import ConnectionPatch
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import ArrowStyle
from matplotlib.patches import Ellipse
from matplotlib.patches import ConnectionStyle
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import BoxStyle
from matplotlib.patches import PathPatch
from matplotlib.patches import FancyArrow
from matplotlib.patches import Arrow
from matplotlib.patches import YAArrow
from matplotlib.patches import CirclePolygon
