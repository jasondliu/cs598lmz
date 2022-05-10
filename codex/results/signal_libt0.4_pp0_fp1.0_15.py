import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from PyQt5.QtCore import QUrl, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType

from mainwindow import MainWindow
from settings import Settings
from downloadmanager import DownloadManager
from downloaditem import DownloadItem
from torrent import Torrent
from torrentmodel import TorrentModel
from torrentproxymodel import TorrentProxyModel
from torrentfilterproxymodel import TorrentFilterProxyModel
from torrentmanager import TorrentManager
from torrentstatus import TorrentStatus
from torrentpriority import TorrentPriority
from torrentcategory import TorrentCategory
from torrentfile import TorrentFile
from torrentfilemodel import TorrentFileModel
from torrentfileproxymodel import TorrentFileProxyModel
from torrentfilefilterproxymodel import TorrentFileFilterProxyModel
from torrentpeersmodel import TorrentPeersModel
from torrentpeer import TorrentPeer
from torrenttrackermodel import TorrentTrackerModel
from torrenttracker import TorrentTracker
from torrenttr
