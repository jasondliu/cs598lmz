import gc, weakref
import numpy as np
import numpy.random as rng
import scipy.sparse as sp
import scipy.sparse.linalg as spl
import scipy.linalg as la
import scipy.integrate as quad
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec
import matplotlib.widgets as widgets
import matplotlib.transforms as transforms
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.colorbar as colorbar
from matplotlib.collections import PatchCollection
import matplotlib.lines as mlines
from mpl_toolkits.axes_grid1 import make_axes_locatable
from
