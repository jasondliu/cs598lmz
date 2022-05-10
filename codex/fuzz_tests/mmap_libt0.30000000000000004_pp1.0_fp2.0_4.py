import mmap
import os
import re
import sys
import time

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version

# TODO:
# - Add a test for the case where the user has a custom .bashrc that sources
#   the system .bashrc.
# - Add a test for the case where the user has a custom .bashrc that sources
#   the system .bashrc and the system .bashrc sources the system .bash_profile.
# - Add a test for the case where the user has a custom .bashrc that sources
#   the system .bashrc and the system .bashrc sources the system .bash_profile
#   and the system .bash_profile sources the system .profile.
# - Add a test for the case where the user has a custom .bashrc that sources
#   the system .bashrc and the system .bashrc sources the system .bash_profile
#   and the system .bash_profile sources the system .profile and the system
#   .profile sources the system .bash_login.

