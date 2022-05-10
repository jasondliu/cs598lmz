import signal
signal.signal(signal.SIGINT, lambda n, f: sys.exit(0))

from math import *
import numpy.random as random
#from constants import *
from misc import *
import bisect
from Mesh import *
from MyVector import *
from Vertex import *
from Edge import *
from Face import *
from Polyhedron import *
import copy

"""
def isSamePoint(p0,p1):
    if not (p1.x==p0.x):
        return False
    if not (p1.y==p0.y):
        return False
    if not (p1.z==p0.z):
        return False
    return True
"""

#G = {}

################################################==========
def getRandomVector():
    r= [2.0*(random.random_sample()-0.5),2.0*(random.random_sample()-0.5),2.0*(random.random_sample()-0.5)]
