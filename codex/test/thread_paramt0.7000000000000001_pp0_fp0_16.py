import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()
# Above line clears terminal when cell is run

import random as rnd
import matplotlib.pyplot as plt
 

# Initial Conditions
#   1. location of the agent (x,y)
#   2. agent's velocity (vx,vy)
#   3. agent's direction (theta)
x,y,vx,vy,theta = 0,0,0,0,0

# Environment
#   1. x-limits of the world
#   2. y-limits of the world
#   3. number of obstacles
#   4. list of obstacles
xmin,xmax,ymin,ymax,num_obstacles,obstacles = 0,0,0,0,0, []

# Navigation
#   1. step size
#   2. minimum distance between agent and obstacle
step_size,min_dist = 0,0

# Visualization
#   1. number of frames per second
fps = 0

# Randomization
