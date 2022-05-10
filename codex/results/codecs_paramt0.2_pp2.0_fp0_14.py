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
import tempfile
import time
import warnings

# Our own imports
from IPython.config.loader import Config
from IPython.core.application import BaseIPythonApplication
from IPython.core.completer import IPCompleter
from IPython.core.error import TryNext
from IPython.core.interactiveshell import InteractiveShell
from IPython.core.profiledir import ProfileDir
from IPython.core.usage import interactive_usage, default_banner
from IPython.utils import io
from IPython.utils.importstring import import_item
from IPython.utils.path import get_ipython_dir
from IPython.utils.process import abbrev_cwd
