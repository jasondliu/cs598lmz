import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def chisq_fit(x,y,error,params,cb=None,fixpars=None,fixparams=None,
              a0=rminsq=None,a1=None,return_a=False):
    """
    Linear fit *y = a + b * x*, with chisq calculation

    Takes in *x*, *y*, *error* and *params* - the y-intercept and slope,
    respectively.  Returns *a*, *b* and the value of chi-square.

    If a callback function is specified by the *cb* argument, it will be
    called after each iteration.

    Optionally takes:

    - *fixpars* - a list of indices of parameters to fix
    - *fixparams* - a list of fixed parameters
    - *a0*, *a1* - guesses for the two parameter values
    - *rminsq* - a function which takes a linear model and the data,
      does the rms calculation, and returns the rms.  the "guess" for
