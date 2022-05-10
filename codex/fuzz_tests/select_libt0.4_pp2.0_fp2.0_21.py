import selectors
import sys

from . import __version__
from . import client
from . import common
from . import config
from . import constants
from . import exceptions
from . import log
from . import messages
from . import server
from . import utils


def _parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="pwncat",
        description="A reverse shell utility with advanced features",
        epilog=constants.EPILOG,
    )
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version="%(prog)s {}".format(__version__),
        help="Show the version and exit",
    )
    parser.add_argument(
        "--debug",
        "-d",
        action="store_true",
        help="Enable debug logging",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging",
    )
    parser.add
