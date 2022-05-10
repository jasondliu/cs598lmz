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

    def __init__(self, host=None, port=None, timeout=None,
                 max_retries=None, retry_interval=None,
                 retry_backoff=None, retry_jitter=None,
                 retry_on_status=None, retry_on_timeout=None,
                 verify_ssl=None, ca_certs=None,
                 client_cert=None, client_key=None,
                 username=None, password=None,
                 token=None, token_update_interval=None,
                 token_update_callback=None,
                 token_update_callback_kwargs=None,
                 token_update_callback_args=None,
                 token_update_callback_on_failure=None,
                 token_update_callback_on_failure_kwargs=None,
