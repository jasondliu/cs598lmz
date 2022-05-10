import socket
import sys
import time

from . import exceptions
from . import protocol
from . import util


class Connection(object):
    """A connection to a single Redis server.

    :param host: Redis host.
    :param port: Redis port.
    :param db: Database ID.
    :param password: Password for the Redis server.
    :param socket_timeout: Socket timeout in seconds.
    :param socket_connect_timeout: Socket connect timeout in seconds.
    :param socket_keepalive: Whether to enable TCP keep-alive.
    :param socket_keepalive_options: Arguments for TCP keep-alive.
    :param socket_type: Socket type.
    :param retry_on_timeout: Whether to retry on connection timeout.
    :param encoding: Encoding for unicode.
    :param encoding_errors: Error handling scheme for unicode encoding.
    :param decode_responses: Whether to decode replies from Redis.
    :param parser_class: Class for parsing replies.
    :param socket_read_size: Read buffer size.

