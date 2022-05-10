import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

################################################################################
# define the objective
################################################################################
def t(x):
    return np.tanh(x)

def tp(x):
    return 1.0 - np.power(np.tanh(x),2)

def tpp(x):
    return -2*np.tanh(x)*(1.0 - np.power(np.tanh(x),2))

def f(x):
    #return np.power(np.sin(x),2)
    return np.power(np.tanh(x),2)

def fp(x):
    #return 2*np.sin(x)*np.cos(x)
    return 2*np.tanh(x)*(1.0 - np.power(np.tanh(x),2))

def fpp(x):
    #return 2*(np.cos(x)*np.cos(x) - np.sin(x)*np.sin(x))
    return 2*(1.0
