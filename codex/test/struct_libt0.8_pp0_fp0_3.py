import _struct
import _thread

import __random
import _socket

# functions

def atexit(func_or_tuple_of_funcs):
    """
    Register a function to be executed upon normal program termination.
    
    func_or_tuple_of_funcs
      A function, or a tuple of functions, that will be executed upon normal
      program termination.  The function(s) are called with no arguments.
    
    If more than one function has been registered, they are executed in the
    reverse order of their registration (i.e. the last registered function is
    the first to be executed).
    
    If an exception is raised in a registered function, the exception is
    ignored and the remaining registered functions are still executed.  If
    the exception is SystemExit, it is re-raised.
    
    If the return value of an executed function is an integer, it will be
    used as the exit code and SystemExit will be raised with that code.
    
    Registration of a new function replaces any previously registered
    function(s).
    """

    pass

