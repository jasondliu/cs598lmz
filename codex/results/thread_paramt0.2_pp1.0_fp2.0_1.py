import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random
import math

# Global variables

# Number of rows and columns
n_rows = 10
n_cols = 10

# Number of agents
n_agents = 10

# Number of iterations
n_iterations = 100

# Number of iterations per frame
n_iterations_per_frame = 1

# Number of frames
n_frames = int(n_iterations / n_iterations_per_frame)

# Number of iterations per second
n_iterations_per_second = 1

# Number of seconds per frame
n_seconds_per_frame = 1 / n_iterations_per_second

# Number of seconds per iteration
n_seconds_per_iteration = 1 / n_iterations_per_second

# Number of seconds per iteration
n_seconds_per_iteration = 1 / n_iterations_per_second

# Number of seconds
