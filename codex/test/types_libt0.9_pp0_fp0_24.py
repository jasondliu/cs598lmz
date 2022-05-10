import types
types.ClassType = type

from mpi4py import MPI
import numpy as np
from numpy import asarray, reshape, ones, sqrt, zeros
from scipy import integrate, sparse
from scipy.sparse import coo_matrix
from expokit import cyexpokit
import math

from Utils import *


class IProbabilityVectorKleinGordon(object):
    """
    Interface specifying the Klein-Gordon probability measurements
    i.e. any operator A satisfying <x(t)|A|psi(t)> = <psi(t)|A|psi(t)>
    """

    def __init__(self, t=0):
        self.t = t


class IProbabilityVectorSchrodinger(object):
    """
    Interface specifying the Schrodinger probability measurements
    i.e. any operator A satisfying <x(t)|A|psi(t)> = <psi(t)|A^dagger A|psi(t)>
    """

