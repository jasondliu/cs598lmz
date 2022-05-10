import gc, weakref
import numpy as np
import numpy.linalg as la
import scipy.linalg as sla
import scipy.sparse.linalg as spla
import scipy.sparse as sp
import scipy.optimize as opt
import scipy.interpolate as interp
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.patches import Polygon
from matplotlib.gridspec import GridSpec
from matplotlib.widgets import Slider, Button, RadioButtons
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib import animation
from matplotlib.offsetbox import OffsetImage,
