import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import QT
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# Import Python libs
import sys
import os
import time
import json
import threading
import traceback
import logging
import logging.handlers
import subprocess

# Import our modules
import core.config
import core.logger
import core.network
import core.utils
import core.updater
import core.web
import core.notifications
import core.settings
import core.plugins
import core.shortcuts
import core.tray
import core.overlay
import core.screenshot
import core.window
import core.browser
import core.downloads
import core.tabs
import core.history
import core.bookmarks
import core.passwords
import core.cookies
import core.settings
import core.downloads
