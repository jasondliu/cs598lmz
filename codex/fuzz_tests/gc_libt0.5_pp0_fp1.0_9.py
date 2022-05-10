import gc, weakref
import sys, os
import random
import math
import time
import copy
import warnings
import pygame
import pygame.locals
import numpy as np
import pandas as pd
from collections import defaultdict
from itertools import product
from shapely.geometry import Point, Polygon, LineString
from shapely.ops import linemerge, polygonize
from shapely.affinity import translate
from shapely.algorithms.polylabel import polylabel
from shapely.validation import explain_validity
from shapely.prepared import prep
from shapely.ops import cascaded_union
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.colors import to_hex, to_rgb
from sklearn.cluster import KMeans

# =============================================================================
#                                                                  LOAD_MAPDATA
# =============================================================================
def load_mapdata(map_name, map_folder=None,
                 map_scale=None, map_size=None,
                 plot
