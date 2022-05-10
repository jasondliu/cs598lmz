import mmap
import os
import re
import shutil
import sys
import tempfile
import time
import urllib2
import zipfile

from src import constants
from src import utils

def _get_path_to_chrome_profile_dir(chrome_path):
    """Get the path to the profile directory of the Chrome installation at
    |chrome_path|.

    The profile directory is the directory containing the user data.

    The path to the profile directory is determined using the command line
    argument '--user-data-dir' of the Chrome executable at |chrome_path|.
    """
    # Get the command line options of the Chrome executable.
    chrome_cmd_line_opts = utils.get_command_line_options(chrome_path)

    # Get the path to the profile directory.
    chrome_profile_dir = chrome_cmd_line_opts['--user-data-dir']

    return chrome_profile_dir

def _get_path_to_chrome_extension_dir(chrome_path):
    """Get the path to the extension directory of the Chrome installation at
