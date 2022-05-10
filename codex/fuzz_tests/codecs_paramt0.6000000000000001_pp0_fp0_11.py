import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This is a workaround to allow the use of the same codebase with
# Python versions 2 and 3.
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

import pkg_resources

from . import __version__
from . import __author__
from . import __copyright__
from . import __license__


class Config(object):
    """
    Config class with the following attributes:

    * ``repo_path``: Path to the git repository.
    * ``repo_url``: URL of the git repository.
    * ``main_branch``: Name of the main branch.
    * ``config_file``: Path to the config file.
    * ``debug_mode``: If True, debug mode is enabled.
    * ``log_file``: Path to the log file.
    * ``log_format``: Format of the log messages.
    * ``log_level``: Level of the log messages.
    * ``log_datefmt``: Format of the date in the log
