import gc, weakref
from mpi4py import MPI
import numpy as np
import numpy.linalg as la
from numpy.linalg import LinAlgError
from scipy.linalg import eigh
from scipy.optimize import minimize
from scipy.optimize import basinhopping
from scipy.optimize import differential_evolution
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.sparse import csr_matrix, eye
from scipy.sparse.linalg import eigsh
from scipy.sparse.linalg import LinearOperator
from scipy.sparse.linalg import eigs
from scipy.sparse.linalg import lobpcg
from scipy.sparse.linalg import ArpackNoConvergence
from scipy.sparse.linalg import ArpackError
import time
import copy
import pickle
import os
import sys
import re
import glob
import multiprocessing
from funct
