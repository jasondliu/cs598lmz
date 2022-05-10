import weakref

import requests

from . import config
from . import exceptions
from . import log
from . import types
from . import utils

_LOG = log.get_logger(__name__)


class Session(object):
    """
    A session object that is used to communicate with the DataRobot API.

    :param str endpoint: The base DataRobot endpoint to use for the session.
    :param str token: The API token to use for the session.
    :param str username: The username to use for the session.
    :param str password: The password to use for the session.
    :param str project_id: The default project ID to use for the session.
    :param str model_id: The default model ID to use for the session.
    :param bool log_to_console: Whether to log to the console.
    :param str log_path: The path to the log file.
    :param str log_level: The log level to use.
    """

