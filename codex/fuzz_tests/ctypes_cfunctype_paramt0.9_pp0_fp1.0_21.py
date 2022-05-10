import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def convert_function(function):
    ''' Convert a function to a ctypes.CDLL with a ctypes.CFUNCTYPE
        FuncType as entry point.
    '''
    my_c_function = FUNTYPE(function)
    dll = ctypes.CDLL(None)
    dll.entry = my_c_function
    return dll

def find_roots(arguments, lower_bound, upper_bound,
               results_are_bounded=True, epsilon=None):
    ''' Find roots of a function using a python script with ctypes
        The script has to compute f(x) = 0 for every x in arguments.

        Arguments:
            A list of floats to be given to the function
            lower_bound and upper bound for the optimization
            results_are_bounded: indicates whether the user guarantees that
            results are in the interval
            epsilon: used as stopping criterium of the optimization

        Returns:
            A list of results
    '''
    if results_are_bounded:
