import codecs
codecs.register_error('surrogate_or_unknown', codecs.surrogateescape, 'surrogate_or_unknown')

import os
import re
import sys
import shlex
import types
import struct
import inspect
import warnings

from subprocess import Popen, PIPE, STDOUT

from ._compat import *
from .util import *
from . import exception

__all__ = [
    'Cmd',
    'Command',
    'CommandType',
    'Shell',
    'ShellType',
    'Pipe',
    'PipeType',
    'Redirect',
    'RedirectType',
    'Redirection',
    'RedirectionType',
    'PipeRedirect',
    'PipeRedirectType',
    'CommandRedirect',
    'CommandRedirectType',
    'ShellRedirect',
    'ShellRedirectType',
    'Process',
    'Stream',
    'StreamType',
]

#------------------------------------------------------------------------------#
# Command                                                                      #
#------------------------------------------------------------------------------#
class Command (object):
    """
    Command is
