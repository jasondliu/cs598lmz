import types
types.ModuleType.__dict__.update(dict)

# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import math
import time
import os
import sys
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
import matplotlib.patheffects as PathEffects
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import NullFormatter
from matplotlib.ticker import LogLocator

