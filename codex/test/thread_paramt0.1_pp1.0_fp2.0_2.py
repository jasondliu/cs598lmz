import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.patheffects as path_effects
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
from matplotlib.collections import PatchCollection
from matplotlib.collections import LineCollection
from matplotlib.collections import PathCollection
from matplotlib.collections import RegularPolyCollection
from matplotlib.collections import PolyCollection
from matplotlib.collections import QuadMesh
from matplotlib.collections import TriMesh
from matplotlib.collections import CircleCollection
from matplotlib.collections import EllipseCollection
from matplotlib.collections import Barbs
from matplotlib.collections import Arrow
from matplotlib.collections import StarPolygonCollection
from matplotlib.collections import Polygon

