import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16
 
#===========================
# model parameters  
#===========================
# grid number
nx = 51
# spatial step size
dx = 0.1
# time steps
nt = 3
# time step size
dt = 0.01
# CFL by default
c = 1

#=================================
# boundary and initial conditions
#=================================
# boundary conditions
xmin = 0.0
xmax = 1.0
u_L = 1.0
u_R = 0.0

# initial condition
def u_0(x):
    """
    initial velocity profile
    """
    if x >= 0.5:
        return 0.0
    else:
        return 1.0

 
#====================================
# analytical solution at time t
#=================================
