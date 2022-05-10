import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

import sys
import os

from . import utils
from . import config
from . import settings
from . import preferences
from . import qtutils
from . import resources
from . import icons
from . import textwrap
from . import core
from . import git
from . import gitcmds
from . import hotkeys
from . import qtcompat
from . import qtlib
from . import cola
from . import coladialogs
from . import cola_bookmarks
from . import cola_commitmsg
from . import cola_diff
from . import cola_merge
