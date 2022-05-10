fn = lambda: None
# Test fn.__code__.co_varnames to see if we're in a function
# with keyword arguments.
fn.__code__.co_varnames = ('a', 'b', 'c', 'd')

try:
    fn.__code__.co_varnames = ('a', 'b', 'c', 'd', 'e')
    HAVE_KWARGS = True
except TypeError:
    HAVE_KWARGS = False

# Test fn.__code__.co_varnames to see if we're in a function
# with keyword arguments.
fn.__code__.co_varnames = ('a', 'b', 'c', 'd')

try:
    fn.__code__.co_varnames = ('a', 'b', 'c', 'd', 'e')
    HAVE_KWARGS = True
except TypeError:
    HAVE_KWARGS = False

def _get_arg_names(func):
    """Return a list of the argument names for a callable.

    Parameters
    ----------
    func : callable
        The call
