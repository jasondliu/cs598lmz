import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

# sys.path.append('./source')

from source.solver import Solver
from source.utils import *

# import the solver
solver = Solver()

# set the initial state
solver.set_initial_state(
    initial_state_type='gaussian',
    initial_state_params=[0.0, 0.1]
)

# set the potential
solver.set_potential(
    potential_type='harmonic',
    potential_params=[1.0]
)

# set the time step
solver.set_time_step(0.01)

# set the time range
solver.set_time_range(0.0, 50.0)

# set the wave function
solver.set_wave_function(
    wave_function_type='gaussian',
