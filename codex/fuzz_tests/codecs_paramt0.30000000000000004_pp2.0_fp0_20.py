import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-----------------------------------------------------------------------------
#  Copyright (C) 2008-2009  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Stdlib
import __builtin__
import __future__
import atexit
import bdb
import codeop
import dis
import inspect
import os
import pdb
import re
import shlex
import shutil
import signal
import socket
import sys
import tempfile
import time
import traceback
import types
import warnings

# Our own packages
from IPython.core import debugger
from IPython.core import oinspect
from IPython.core import page
from IPython.core import prefilter
from IPython.core import release
from IPython.core import ultratb
from IPython.core.error import TryNext
from IPython.core.extensions import ExtensionManager
from IPython.core.fake
