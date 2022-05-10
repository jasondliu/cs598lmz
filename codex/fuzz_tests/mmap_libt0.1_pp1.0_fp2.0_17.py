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

_log = log.get_logger(__name__)

# -----------------------------------------------------------------------------

class _Base(object):
    """
    Base class for all objects.
    """

    def __init__(self, **kwargs):
        """
        Initialize the object.
        """
        self._init_attrs(**kwargs)

    def _init_attrs(self, **kwargs):
        """
        Initialize the object's attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        """
        Return the object's representation.
        """
        return '%s(%s)' % (self.__class__.__name__,
                           ', '.join('%s=%r' % (key, getattr(self,
