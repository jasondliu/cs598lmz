import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os
import time
import glob
import numpy as np
import traceback

#
# Import the module with the global variables
#

import config as cfg

#
# Import the functions
#

import database as db
import utils
import transfer
import test

#
# Constants
#

#
# Variables
#

#
# Functions
#

def main():
    #
    # Init
    #

    # Camera
    camera = None

    #
    # Open the database
    #
    if cfg.database is not None:
        cfg.database = db.open_db()
        if cfg.database is None:
            return None
    else:
        cfg.database = None

    #
    # Test the database
    #
    
    if cfg.database is not None:
        rc = test.test_database(cfg.database)
        if not rc:
            return None

    #
    #
