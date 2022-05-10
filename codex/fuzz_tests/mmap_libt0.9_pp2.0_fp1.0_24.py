import mmap
import numpy as np
import nlopt
import scipy.optimize
import tempfile

from . import utils

class Optimizer:
    """An optimizer class that uses nlopt to optimize the sum of squares of CSD
    values for a model to match a desired set of CSD values.

    The following model properties are available for optimization:
    * AMPA receptor conductance decay time constant.
    * AMPA receptor conductance rise time constant.
    * NMDA receptor conductance decay time constant.
    * NMDA receptor conductance rise time constant.
    * ratio of NMDA receptor to AMPA receptor conductances.
    * the synaptic weight of the AMPA and NMDA receptors.

    In addition to local searches (L-BFGS-B and COBYLA), this class also
    supports global searches (BOBYQA and DIRECT), and parallel
    asynchronous stochastic gradient descent with randomized BOBYQA subproblem
    warmstarts (ANN).

    Convergence status strings are adapted from the output of pyGMO's
    get_status() method, at https://esa.github.
