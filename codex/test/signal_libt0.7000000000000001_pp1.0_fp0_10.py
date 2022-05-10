import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # Handle Ctrl-C

import sys
import time

import numpy as np
import scipy.sparse
import matplotlib.pyplot as plt

# PySPH base and carray imports
from pysph.base.kernels import QuadraticSpline
from pysph.base.utils import get_particle_array_swe as gpa_swe

# PySPH solver and integrator
from pysph.solver.application import Application
from pysph.solver.solver import Solver
from pysph.sph.integrator import PECIntegrator
from pysph.sph.integrator_step import WCSPHStep

# Numerical schemes
from pysph.sph.scheme import SchemeChooser
from pysph.sph.wc.basic import WCSPHScheme

# PySPH sph evaluator for forces
from pysph.sph.equation import Group

