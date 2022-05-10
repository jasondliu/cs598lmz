import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-----------------------------------------------------------------------------
#  Copyright (C) 2013 The IPython Development Team
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
from IPython.utils import py3compat
from IPython.utils.importstring import import_item
from IPython.utils.path import get_ipython_dir
from IPython.utils.process import getoutput
from IPython.utils.traitlets import (
    Bool, Dict, Unicode, Instance, List,
)
from IPython.utils.warn import error

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Local utilities
#-----------------------------------------------------------------------------

def get_default_editor():
    """Get the default editor for the system."""
    # This is a list of (OS, editor)
