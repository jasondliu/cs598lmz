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

_logger = log.get_logger(__name__)


class _Base(object):
    """Base class for all objects."""

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__,
                            ' '.join('%s=%r' % (k, v)
                                     for k, v in self._kwargs.items()))


class _BaseWithName(_Base):
    """Base class for all objects with a name."""

    def __init__(self, name, **kwargs):
        super(_BaseWithName, self).__init__(**kwargs)
        self.name = name


class _BaseWithNameAndIcon(_BaseWithName):
    """Base class for
