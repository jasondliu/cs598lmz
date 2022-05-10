import ctypes
ctypes.CDLL('KpClib.so', mode=ctypes.RTLD_GLOBAL)
from KpClib import *

import numpy as np
from scipy.constants import c, e, m_e
import matplotlib.pyplot as plt
from matplotlib import gridspec
import math
from mpi4py import MPI
import sys

from PyPARIS_sim_class import Sim, fodo_lattice
from PyHEADTAIL_feedback.processors.fodo_feedback import FODOFeedback
from PyHEADTAIL_feedback.processors.transverse_damper import TransverseDamper
from PyHEADTAIL_feedback.processors.sum_feedback import SumFeedback
from PyHEADTAIL_feedback.processors.transverse_damper import TransverseDamper
from PyHEADTAIL_feedback.processors.transverse_damper import TransverseDamper
from PyHEADTAIL_feedback.processors.transverse_kick_smoother import TransverseKickSmoother

from PyHEADTAIL_
