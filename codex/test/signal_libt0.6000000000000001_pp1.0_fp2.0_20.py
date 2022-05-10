import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL

from cola import cmds
from cola import core
from cola import gitcmds
from cola import hotkeys
from cola import icons
from cola import qtutils
from cola import resources
from cola import settings
from cola import utils
from cola import version
from cola.i18n import N_
from cola.widgets import completion
from cola.widgets import defs
from cola.widgets import standard
from cola.models import prefs

from cola.views import about
from cola.views import compare
from cola.views import create
from cola.views import diff
from cola.views import grep
from cola.views import preferences
from cola.views import update

# This widget uses a QStackedLayout to manage different views
#
