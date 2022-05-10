import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import time
import shutil
import subprocess
import tempfile
import logging
import logging.handlers

import yaml
import requests
import click
import jinja2

from . import __version__
from . import __author__
from . import __email__
from . import __url__
from . import __license__
from . import __copyright__

from . import utils
from . import exceptions
from . import config
from . import logger
from . import constants
from . import templates
from . import plugins
from . import __main__ as main


def _get_logger(name, level=logging.DEBUG, logfile=None):
    """
    Get a logger.

    :param str name: Logger name.
    :param int level: Logger level.
    :param str logfile: Log file path.
    :returns: Logger object.
    :rtype: logging.Logger
    """
    log = logging.getLogger(name)
    log
