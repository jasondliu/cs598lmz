import weakref
import copy
from math import sqrt
import numpy as np

def distance(point1, point2):
    """ Calculate the distance between two points """
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

#from scipy.spatial.distance import cdist
from scipy.spatial import distance as dist


class KMeans:

    """ Implementation of the k-means algorithm """

    def __init__(self, n_clusters=1, points=None, max_iterations=100):
        """
        Initialize the k-means algorithm with the given parameters. If no points are given, they can be added later.
        :param n_clusters: Number of clusters to calculate.
        :param points: A set of points to be clustered.
        :param max_iterations: Maximum number of iterations per run.
        """
        self.n_clusters = n_clusters
        self.points = points
        self.initial_points = points
        self
