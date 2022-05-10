import mmap
import os
import re
import sys
import time
import traceback

from . import __version__
from . import config
from . import log
from . import util
from . import xdg

# -----------------------------------------------------------------------------
# Globals

_log = log.get_logger(__name__)

# -----------------------------------------------------------------------------
#

class Error(Exception):
    pass

# -----------------------------------------------------------------------------
#

class _Base(object):
    """
    Base class for all objects.
    """

    def __init__(self, **kwargs):
        """
        Initialize the object.
        """
        self._init(**kwargs)

    def _init(self, **kwargs):
        """
        Initialize the object.
        """
        pass

    def __repr__(self):
        """
        Return a string representation of the object.
        """
        return '<%s>' % self.__class__.__name__

# -----------------------------------------------------------------------------
#

class _Config(_Base):
    """
    Base class for all objects that have a configuration
