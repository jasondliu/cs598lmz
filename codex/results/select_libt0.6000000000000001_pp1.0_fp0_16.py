import select
import sys
import traceback

from pykeepass import PyKeePass

from . import __version__
from . import config


def handle_connection(connection, path):
    """Serve the given connection."""
    try:
        request_line = connection.readline()
    except ValueError:
        return

    if not request_line:
        return

    request_line = request_line.decode('utf-8').rstrip()
    request_line = request_line.split()
    request_method = request_line[0]
    request_path = request_line[1]

    if request_method != 'GET' or request_path != '/':
        connection.sendall(b'HTTP/1.1 400 Bad Request\r\n\r\n')
        return

    keepass_file = os.path.expanduser(config.get('keepass', 'file'))
    keepass_password = None

    if os.path.exists(keepass_file):
        with open(keepass_file, 'rb') as f:

