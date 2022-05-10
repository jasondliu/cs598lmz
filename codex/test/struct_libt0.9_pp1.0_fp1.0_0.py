import _struct
import math
import networkx as nx
import numpy as np


def createCorridorGraph(dims, width):
    G = np.zeros(dims)
    w2 = width / 2.
    G[0:width, width:dims[1]-width] = -100.
    G[dims[0]-width:, width:-width] = -100.
    G[width:-w2-1, :width*2] = -100.
    G[width:-w2-1, -width*2:] = -100.

    return G


def createCorridorMaze(dims, width, roomDim, roomCount, maxRoomTries=100, maxTries=100):
    if roomDim[0] > width:
        raise Exception("room dimension can't be larger than width")

    G = createCorridorGraph(dims, width)

    # first create the rooms
    roomNodes = []   # list of left corners of each room
