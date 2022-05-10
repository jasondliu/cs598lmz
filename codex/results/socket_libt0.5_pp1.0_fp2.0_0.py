import socket
from threading import Thread
from os.path import isfile
from os import getcwd
from time import sleep
from pprint import pprint
import argparse

from . import __version__
from . import utils
from . import config
from . import server
from . import client
from . import log
from . import shutdown
from . import __file__ as current_file
from . import __name__ as package_name
from . import __path__ as package_path


def main():
    """
    Main function that starts the server and client.
    """
    # Get current working directory
    cwd = getcwd()

    # Parse arguments
    args = parse_arguments()

    # Get the log level
    log_level = getattr(log, args.log_level.upper())

    # Get the host and port
    host = args.host
    port = args.port

    # Get the path to the file to use
    file_path = args.file_path

    # Get the delay between sending messages
    delay = args.delay

    # Get the shutdown delay
