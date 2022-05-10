import socket
import sys
import time

from . import config
from . import log
from . import utils
from . import version

# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# pylint: disable=too-many-nested-blocks
def main(args):
    """
    Main entry point for the client.
    """
    # Parse the command line arguments
    parser = argparse.ArgumentParser(
        description='The client for the ' + version.NAME + ' ' + version.VERSION)
    parser.add_argument('-c', '--config',
                        help='The configuration file to use')
    parser.add_argument('-d', '--debug',
                        help='Enable debug output',
                        action='store_true')
    parser.add_argument('-v', '--version',
                        help='Print the version and exit',
                        action='store_true')
    parser
