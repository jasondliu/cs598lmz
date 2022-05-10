import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import random
import time
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import TextBox
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import LassoSelector
from matplotlib.widgets import RectangleSelector
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.collections import LineCollection
from matplotlib.collections import PathCollection
from matplotlib.collections import PolyCollection
from matplotlib.collections import QuadMesh
from matplotlib.collections import TriMesh
