import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogateescape)

try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser

import logging
import os
import sys
import traceback

from pkg_resources import resource_filename

from . import __version__, __license__
from . import config
from . import config_defaults
from . import data
from . import event
from . import exceptions
from . import filters
from . import formats
from . import log
from . import network
from . import output
from . import plugin
from . import proxy
from . import schema
from . import util
from . import version
from . import web

logger = logging.getLogger(__name__)


class Application(object):
    """
    The main application object.

    This class is responsible for setting up and running the application.
    """

    def __init__(self, args=None, config_file=None, config_dict=None,
                 config_string=None, config_args=None,
                 debug=False
