import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-----------------------------------------------------------------------------
#  Copyright (C) 2008  The IPython Development Team
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
import time
import warnings

# Our own imports
from IPython.core.error import TryNext
from IPython.core import release
from IPython.utils import io
from IPython.utils.importstring import import_item
from IPython.utils.path import get_ipython_dir
from IPython.utils.process import arg_split
from IPython.utils.py3compat import PY3
from IPython.utils.terminal import toggle_set_term_title
from IPython.utils.traitlets import (
    Bool, CBool, Unicode, Dict, List, Any, Instance, Integer, Float,
)
from IPython.utils.warn import warn
