import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import getopt
import socket
import threading
import subprocess
import traceback
import webbrowser

from PyQt4 import QtCore, QtGui

from twisted.internet import reactor

from Tribler.Core.CacheDB.SqliteCacheDBHandler import ChannelCastDBHandler, TorrentDBHandler
from Tribler.Core.Session import Session
from Tribler.Core.SessionConfig import SessionStartupConfig
from Tribler.Core.TorrentDef import TorrentDef
from Tribler.Core.Utilities.utilities import show_permid_short
from Tribler.Main.globals import DefaultDownloadStartupConfig
from Tribler.Main.vwxGUI import DEFAULT_API_PORT
from Tribler.Main.vwxGUI.GuiImageManager import GuiImageManager
from Tribler.Main.vwxGUI.GuiUtility import GUIUtility
from Tribler.Main.vwxGUI.SearchGridManager import SearchGridManager
