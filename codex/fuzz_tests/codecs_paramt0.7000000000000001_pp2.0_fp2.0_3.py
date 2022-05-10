import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__

#
# Utility functions
#

def _check_package():
    """Check that the package is installed correctly."""
    try:
        exec(textwrap.dedent("""
            from importlib import resources
            resources.read_text(__package__, 'test.txt')
        """))
    except ImportError as e:
        print("Error: Failed to import pkg_resources.  Please make sure that\n"
              "       setuptools is installed.")
        print(e)
        sys.exit(1)
    except FileNotFoundError as e:
        print("Error: Failed to import pkg_resources.  Please make sure that\n"
              "       the package is installed correctly.")
        print(e)
        sys.exit(1)

_check_package()

#
# Import PHOEBE submodules
#

import phoebe
from . import backend
from . import frontend
from . import constraints

from .backend import *
from .frontend
