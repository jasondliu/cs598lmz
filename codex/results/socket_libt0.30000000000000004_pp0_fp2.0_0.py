import socket
import sys
import time

from . import exceptions
from . import utils

logger = logging.getLogger(__name__)


class Connection(object):
    """
    A connection to a remote host.

    :param host: A hostname or IP address.
    :type host: str
    :param port: A port number.
    :type port: int
    :param username: A username.
    :type username: str
    :param password: A password.
    :type password: str
    :param private_key: A private key file path.
    :type private_key: str
    :param private_key_pass: A private key password.
    :type private_key_pass: str
    :param timeout: A timeout in seconds.
    :type timeout: int
    :param keepalive: A keepalive interval in seconds.
    :type keepalive: int
    :param session: A :class:`paramiko.client.SSHClient` instance.
    :type session: :class:`paramiko.client.SSHClient`

