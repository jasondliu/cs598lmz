import select

from . import util
from . import config
from . import exceptions
from . import constants

import logging
logger = logging.getLogger(__name__)

class Client(object):
    def __init__(self, host, port, username=None, password=None,
                 use_ssl=False, ssl_verify=True, ssl_cert=None,
                 ssl_key=None, ssl_ca_cert=None, timeout=None,
                 auth_mechanism='PLAIN',
                 reconnect=False, reconnect_max_attempts=3,
                 reconnect_delay=1.0, reconnect_backoff=1.0,
                 reconnect_jitter=0.0,
                 ssl_context=None,
                 **kwargs):
        """
        Create a new :class:`Client` instance.

        :param str host: hostname or IP address of the RabbitMQ server
        :param int port: port number of the RabbitMQ server
        :param str username: username for authentication
        :param str password: password for authentication
        :param
