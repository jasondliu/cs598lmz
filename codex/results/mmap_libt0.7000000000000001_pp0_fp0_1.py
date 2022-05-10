import mmap
import os
import re
import sys
import time
import psutil

from subprocess import Popen, PIPE
from multiprocessing import Process, Queue

# local imports
from . import utils
from . import constants


def get_file_type(file_path):
    """
    Get the file type of the input file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: File type. If no file type is found, returns 'other'.
    """
    if os.path.exists(file_path):
        command = ['file', file_path]
        popen = Popen(command, stdout=PIPE, stderr=PIPE)
        out, err = popen.communicate()
        if popen.returncode == 0: # file command succeeds
            # example, out will be:
            #   /path/to/file: gzip compressed data, was "file", last modified: Tue Feb 18 17:35:52 2020, from Unix
            lines = out.decode('
