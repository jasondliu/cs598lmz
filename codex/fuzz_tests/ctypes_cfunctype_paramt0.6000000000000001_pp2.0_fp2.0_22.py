import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))

from . import _c_solver

class Solver(object):
    """
    Solver object is used to integrate ODE systems.

    Keyword arguments:
    dt -- time step (default: 0.1)
    t_start -- start time (default: 0.0)
    t_stop -- stop time (default: 1.0)
    """

    def __init__(self, dt=0.1, t_start=0.0, t_stop=1.0):
        self.dt = dt
        self.t_start = t_start
        self.t_stop = t_stop

        self.fun = None
        self.y0 = None
        self.t = []

    def set_fun(self, fun, y0):
        """
        Set function to integrate.

        Arguments:
        fun -- function to be integrated
        y0 -- initial conditions
        """

        self.fun = FUNTYPE(fun)
        self.y0
