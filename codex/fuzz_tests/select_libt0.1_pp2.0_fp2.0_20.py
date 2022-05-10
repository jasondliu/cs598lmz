import select
import socket
import sys
import time
import traceback

from . import __version__
from . import config
from . import log
from . import util
from . import x11
from . import xkb
from . import xorg
from . import xrandr
from . import xserver

# -----------------------------------------------------------------------------
# Globals

# -----------------------------------------------------------------------------
# Functions

def main():
    """
    Main function.
    """

    # Parse command line arguments.
    parser = argparse.ArgumentParser(
        description="X11 keyboard layout switcher",
        epilog="""
            The configuration file is searched for in the following locations:
            %s
            """ % config.get_config_file_locations(),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "-c", "--config",
        help="configuration file")
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="enable debug output")
    parser.add_argument(
        "-
