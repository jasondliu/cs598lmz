import weakref
import logging
import sys
import traceback
import os

from . import errors
from . import util
from . import constants
from . import events
from . import config

log = logging.getLogger(__name__)

class BaseConnection(object):
    """
    Base class for all connection types.
    """

