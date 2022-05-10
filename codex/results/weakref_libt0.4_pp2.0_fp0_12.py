import weakref
import time
import logging
import threading

from . import utils
from . import events
from . import errors
from . import protocol
from . import api

logger = logging.getLogger(__name__)


class Client(object):
    """
    Represents a connection to a remote host.

    :param host: The hostname to connect to.
    :param port: The port to connect to.
    :param user: The username to authenticate as.
    :param password: The password to authenticate with.
    :param database: The database to connect to.
    :param ssl: If ``True``, connect using SSL.
    :param ssl_verify: If ``True``, verify the server's SSL certificate.
    :param ssl_ca_certs: Path to a file containing the CA certificates to use
        for SSL verification.
    :param ssl_certfile: Path to a file containing the client certificate to
        use for SSL verification.
    :param ssl_keyfile: Path to a file containing the client private key to
        use for SSL verification.
