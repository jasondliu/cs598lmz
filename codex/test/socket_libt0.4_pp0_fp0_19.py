import socket
import sys
import time

from . import __version__
from . import config
from . import exceptions
from . import log
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_logger.info('{} {}'.format(__name__, __version__))


class _Mock(object):
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return _Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            mockType = type(name, (), {})
            mockType.__module__ = __name__
            return mockType
        else:
            return _Mock()


