import mmap
import os
import sys
import time

from . import common
from . import config
from . import constants
from . import errors
from . import interfaces
from . import util
from . import validators
from . import version
from . import vt100
from . import vt220
from . import vt52
from . import xterm
from . import xterm256
from . import xterm88
from . import xterm_rgb
from . import xterm_truecolor
from . import xterm_truecolor_rgb


LOGGER = logging.getLogger(__name__)


def _get_control_sequence_by_name(name):
    """
    Return a control sequence by name.

    Args:
        name (str): The name of the control sequence.

    Returns:
        str: The control sequence.

    """
    for key in constants.CONTROL_SEQUENCES:
        if key.lower() == name.lower():
            return constants.CONTROL_SEQUENCES[key]

    return None


def _get_control_sequence
