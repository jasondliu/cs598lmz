import mmap
import os
import re
import sys
import tempfile
import time
import traceback

from . import __version__
from . import config
from . import constants
from . import errors
from . import utils
from . import vcs
from . import worker
from . import xdg

#-----------------------------------------------------------------------------
# Globals

# The default logger is a no-op
logger = logging.getLogger('pip')

#-----------------------------------------------------------------------------
# Main functions

def main(initial_args=None):
    """
    The main function.  This handles the command line arguments
    and then runs the subcommand that was selected.
    """
    # Configure our deprecation warnings to be sent through loggers
    from . import deprecated
    deprecated.install_warning_logger()

    # Create the top-level parser.
    parser, options, args = create_main_parser()

    # Parse the command line.
    options, args = parser.parse_args(args=initial_args)
    if options.download_cache:
        os.environ['PIP_DOWN
