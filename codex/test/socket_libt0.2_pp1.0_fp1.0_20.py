import socket
import sys
import time

import requests

from . import utils
from . import config

logger = logging.getLogger(__name__)


class Client(object):
    """
    Client for the API.
    """

