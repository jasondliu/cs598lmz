import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-----------------------------------------------------------------------------
#  Copyright (C) 2013  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Stdlib imports
import os
import sys
import warnings

# Our own imports
from IPython.utils.path import get_ipython_dir
from IPython.utils.process import getoutput
from IPython.utils.py3compat import cast_bytes, str_to_unicode

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Local utilities
#-----------------------------------------------------------------------------

def get_xdg_cache_dir():
    """Get the XDG cache dir for IPython, if it exists.

    Returns None if XDG_CACHE_HOME is not set or empty.
    """
    xdg_cache_home = os.environ.get('XDG_CAC
