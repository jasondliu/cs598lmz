import types
types.SimpleNamespace = SimpleNamespace

import warnings
warnings.simplefilter("ignore", category=DeprecationWarning)

# Ignore this ugly module
import ephem
ephem.__name__ = None

try:
    from IPython import embed as shell
except ImportError:  # Running IPython requires IPython.
    raise Exception("You need IPython to use the shell() function.")

if __name__ == "__main__":

    import doctest
    doctest.testmod()
