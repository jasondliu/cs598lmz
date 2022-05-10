import mmap
import os
import re
import sys
import time
import traceback

from . import __version__
from . import config
from . import log
from . import util
from . import xdg

# The following is a list of all the possible values for the
# "X-GNOME-Bugzilla-ExtraInfoNeeded" key in the desktop file.
#
# If you add a new value, please update the documentation in
# gnome-control-center.xml.in.
EXTRA_INFO_NEEDED_VALUES = [
    'apport-bug',
    'apport-package',
    'apport-version',
    'architecture',
    'command-line',
    'current-settings',
    'date',
    'distribution',
    'error-message',
    'gdb-backtrace',
    'gsettings-schemas',
    'hardware-info',
    'lsb-release',
    'package-version',
    'problem-type',
    'python-traceback',
    'relevant-logs',

