import threading
threading.Thread(target = lambda : execfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'utils', 'slider.py')) ).start()

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph
from pyqtgraph import mkPen

import numpy as np
import pandas as pd
from scipy import ndimage

import maxflow

from skimage import io, segmentation
from skimage.future import graph
from skimage import color
from skimage import morphology
from skimage import filters
from skimage import measure

from sklearn import preprocessing
from sklearn.preprocessing import normalize
from sklearn import decomposition
from sklearn import cluster
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.image import grid_to_graph

from utils import visualization as vis
from utils import misc
from utils import sliding_window
from utils.misc import split_into_smaller_chunks
