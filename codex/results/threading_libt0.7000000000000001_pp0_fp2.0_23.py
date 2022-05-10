import threading
threading.stack_size(512*2048)
sys.setrecursionlimit(10**8)

def _lambda(loc):
    return (1.0/2)*(1+loc)*(1+loc)
def _mu(loc):
    return (1.0/2)*(1-loc)*(1-loc)
def _sigma(loc):
    return (1.0/2)*(1-loc*loc)

'''
    @use:
        The function "initialize_w_params" returns the array holding the
        parameters of the function W. This function is computed by
        three functions, "lambda_operator", "mu_operator", "sigma_operator",
        which are respectively taking the values at the points "1,2,3" and
        "2,3,4". The sum of the three functions is the function W.

    @param:
        N: The number of points given by the user.
        T: The number of time steps given by the user.
        dt: The time step size given by the user.
        dx: The space step size
