import weakref
import time
import os
import sys
import socket
import select
import threading
import traceback
import string
import random
import logging
import logging.handlers
import logging.config

from . import utils
from . import event
from . import config
from . import plugin
from . import command
from . import user
from . import channel
from . import irc
from . import log
from . import server
from . import net
from . import socket
from . import version

class Bot(object):
    """
    The Bot class is the main class of the bot. It contains the main loop and
    all the other classes.
    """
    def __init__(self, config_file=None, log_config=None, log_level=None,
                 log_file=None, log_dir=None, log_format=None, log_datefmt=None,
                 log_style='%', log_max_size=None, log_max_files=None,
                 log_stderr=False, log_stdout=False, log_stdout_level=None,
