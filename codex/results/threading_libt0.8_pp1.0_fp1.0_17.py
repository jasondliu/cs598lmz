import threading
threading.stack_size(67108864)
# sys.setrecursionlimit(2 ** 20)

from random import random
import math
from math import sqrt


def generate_nodes(n=8):
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]

    for i in range(n):
        x[i] = i
        y[i] = i + 1

    return x, y


def generate_edges_from_distance(x, y):
    n = len(x)

    edges_x = []
    edges_y = []
    edges_distances = []

    for i in range(n):
        for j in range(i + 1, n):
            edge_x = []
            edge_y = []
            edge_distance = 0

            edge_x.append(x[i])
            edge_x.append(x[j])

            edge_y.append(y[i])
            edge_y.append(y[j])

            distance = math.sqrt((
