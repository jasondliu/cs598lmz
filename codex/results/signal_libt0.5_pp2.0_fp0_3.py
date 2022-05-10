import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import time
import os
import random
import subprocess
import threading
import webbrowser

from ui_mainwindow import Ui_MainWindow
from ui_aboutdialog import Ui_AboutDialog
from ui_settingsdialog import Ui_SettingsDialog
from ui_dockwidget import Ui_DockWidget
from ui_searchdialog import Ui_SearchDialog
from ui_playlistdialog import Ui_PlaylistDialog
from ui_subtitle_dialog import Ui_SubtitleDialog
from ui_subtitle_download_dialog import Ui_SubtitleDownloadDialog

from settings import Settings
from player import Player
from playlist import Playlist
from subtitle_downloader import SubtitleDownloader

