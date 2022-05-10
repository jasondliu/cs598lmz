import socket
import sys
import time
import threading
import random
import os
import json
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from matplotlib.patches import Polygon
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from matplotlib.collections import LineCollection
from matplotlib.colors import colorConverter
from matplotlib.colors import ListedColormap, BoundaryNorm

# Global variables
global_lock = threading.Lock()
global_time = 0
global_time_lock = threading.Lock()
global_time_step = 0.01
global_time_step_lock = threading.Lock()
global_time_step_min = 0.01
global_time_step_max = 0.1
global_time_step_min_lock
