import mmap
import os
import sys

from . import utils

log = logging.getLogger(__name__)

# We use this for the "unreadable" files
# that we can't get the contents of.
EMPTY_FILE = '<unreadable file>'

# A list of file extensions that we will attempt to treat as text files.
# These are in addition to the built-in python file types.
TEXT_FILE_EXTENSIONS = (
    '.py',
    '.txt',
    '.rst',
    '.conf',
    '.cfg',
    '.ini',
    '.vim',
    '.bat',
    '.sh',
    '.csh',
    '.zsh',
    '.bash',
    '.ksh',
    '.tcl',
    '.lua',
    '.pl',
    '.pm',
    '.php',
    '.php3',
    '.php4',
    '.php5',
    '.php6',
    '.php7',
    '.phtml',
    '.rb',
    '.sql',
    '.css',
    '.
