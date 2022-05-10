import socket
socket.if_indextoname(34)

'''
pip install pydstool

-> Dynamical system toolbox for Python
solves systems numerically and adds state space modelling to Python.

import pydstool as dst
from pydstool import solve
from numpy import linspace

# Step 1: Define a flow

def mysystem(u, t): # u contains the state (x,y,...) of the system
    dydt = [-u[1] + u[0]*(1 - u[0]*u[0] - u[1]*u[1]), \
            u[0] + u[1]*(1 - u[0]*u[0] - u[1]*u[1])]
    return dydt

# Step 2: Create an instance for integration and simulation
start = 0; stop = 20; dt = .01
t = linspace(start, stop, (stop-start)/dt); # Save output every dt units of time

U0 = [-2, 3]   # Initial state, i.e. initial condition


