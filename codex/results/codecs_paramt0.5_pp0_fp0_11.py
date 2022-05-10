import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-----------------------------------------------------------------------------
#  Copyright (C) 2008-2011  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
import sys
import os

# Local imports
from IPython.core.compilerop import CachingCompiler
from IPython.utils.py3compat import PY3

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------


class PyPyCachingCompiler(CachingCompiler):
    """Compile Python code using Psyco, if available.
    """

    def __init__(self):
        CachingCompiler.__init__(self, 'pypy', 'PyPy')
        self.flags = sys.flags
        self.executable = sys.executable

    def _flags(self):
        return sys.flags

    def _executable(self):
        return
