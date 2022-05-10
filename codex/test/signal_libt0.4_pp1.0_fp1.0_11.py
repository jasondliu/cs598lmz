import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qtpy import QtCore

from . import __version__
from . import __appname__
from . import __description__
from . import __url__
from . import __copyright__
from . import __author__
from . import __email__

from . import resources
from . import config
from . import util
from . import icons
from . import widgets
from . import dialogs
from . import settings
from . import lib
from . import mainwindow
from . import browser
from . import search
from . import player
from . import playlist
from . import library
from . import collection
from . import cover
from . import lastfm
from . import edit
from . import tag
from . import info
from . import equalizer
from . import context
from . import devices
from . import remote
