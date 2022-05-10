import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.path as path

from scipy.spatial.distance import euclidean
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances

from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay

from shapely.geometry import Polygon, Point
from shapely.geometry.polygon import LinearRing, LineString

from descartes import PolygonPatch

from matplotlib.collections import PatchCollection

from matplotlib.patches import Polygon as m
