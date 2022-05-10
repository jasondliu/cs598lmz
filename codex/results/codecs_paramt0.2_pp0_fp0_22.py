import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Python 2/3 compatibility
from six import iteritems

# Local imports
from . import util
from . import config
from . import exceptions
from . import constants
from . import compat
from . import log
from . import __version__

# Constants
_LOGGER = log.get_logger(__name__)

# Exceptions
class InvalidConfigError(exceptions.Error):
    """Invalid configuration file."""

# Classes
class Config(object):
    """Configuration object."""

    def __init__(self, filename=None, defaults=None, **kwargs):
        """Initialize configuration object.

        :param filename: Configuration file name.
        :param defaults: Default configuration values.
        :param kwargs: Default configuration values.
        """
        self.filename = filename
        self.defaults = defaults or {}
        self.defaults.update(kwargs)
        self.values = {}
        self.read()

    def read(self):
        """Read configuration file."""
        if self.filename
