import mmap
import re
import os
import os.path
import datetime
import gzip
import subprocess
import docker
import pymongo

# custom imports
import figure
import fstar
import nf
import nf.engine
import nf.action

class Fstar_Exec(nf.action.Action):
    """
    A generic class used to execute F* binaries on a file
    """

    def __init__(self, filename, fstar_path, phases, flags, fst_files,
            log_level=logging.DEBUG, logger=None, timeout=None): #timeout removed to avoid a race condition for long tests
        if logger is None:
            logger = nf.engine.default_logger

        with open(filename, 'r') as f:
            source = f.read()

        self.filename = filename
