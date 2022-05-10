import mmap
import numpy as np
import pdb
import re
import sys
import time
import traceback
import warnings
import yaml

from . import aps
from . import raster
from . import util

from . import cli

###############################################################################

def main():
    """
    The main function.
    """

    # Parse command-line arguments.
    args = cli.parse_args()

