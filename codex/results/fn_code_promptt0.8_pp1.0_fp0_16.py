fn = lambda: None
# Test fn.__code__ removal for 2.2 compatibility
if not hasattr(fn, '__code__') and hasattr(fn, 'func_code'):
    fn.__code__ = fn.func_code

def get_fn_name(fn):
    '''
    Try to get the name of a function, or at least its id
    '''
    try:
        name = fn.__name__
    except AttributeError:
        name = 'fn:%s' % id(fn)
    return name

def get_fn_args(fn):
    '''
    Get the names of the arguments to a function

    Takes in a function, returns a tuple containing the function's
    argument names and a boolean indicating whether or not the function
    takes **kwargs.
    '''
    try:
        fn_code = fn.__code__
    except AttributeError:
        # Function has no __code__ attribute (Python 2.2 compatibility)
        # Lets try to introspect the arguments anyway, hackish but better
        # than nothing.
        return list(inspect.getargspec(
