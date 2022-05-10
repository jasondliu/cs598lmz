import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.colors as colors
import matplotlib.cm as cmx
import pdb
import time
#from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d import Axes3D

plt.rcParams.update({'font.size': 14})

# def create_spherical_data(r, n):
#     """
#     Generate random points on the surface of a sphere
#     :param r: Radius of the sphere
#     :param n: Number of points to generate
#     :return: nx3 array of points that lie on the sphere
#     """
#     xyz = np.random.randn(n, 3)
#     xyz /= np.sqrt(np.sum(xyz ** 2, axis=
