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
from . import cola_prefs
from . import cola_remote
from . import cola_selectcommits
from . import cola_status
from . import cola_tree
from . import cola_widgets
from . import completion
from . import completion_widget
from . import completion_model
from . import completion_view
from . import completion
