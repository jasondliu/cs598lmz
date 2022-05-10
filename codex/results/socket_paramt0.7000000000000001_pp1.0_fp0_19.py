import socket
socket.if_indextoname('1')

# %load_ext autoreload
# %autoreload 2

# %matplotlib inline
# from matplotlib import pyplot as plt
# from matplotlib import animation

# from IPython.display import HTML

import numpy as np

from DataLoader import DataLoader
from DataLoader_pt2 import DataLoader_pt2
from K_Means_pt2 import KMeans_pt2
from K_Means_pt3 import KMeans_pt3
from K_Means_pt4 import KMeans_pt4


def plot_clusters(clusters):
    for i, cluster in enumerate(clusters):
        x, y = cluster.centroid
        plt.scatter(x, y, color='C'+str(i), marker='x')
        plt.scatter(cluster.points[:, 0], cluster.points[:, 1], color='C'+str(i), alpha=0.5)
    plt.show()
    
    
def animate_clusters(clusters):
    fig =
