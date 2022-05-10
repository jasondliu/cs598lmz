import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QApplication, QLabel,
                             QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QProgressBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

from torrent import Torrent
from torrent_thread import TorrentThread
from peer_thread import PeerThread
from torrent_file import TorrentFile
from peer import Peer
import constants as c
from tracker import Tracker


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.file = TorrentFile()
        self.peer_list = []
        self.peers_connected = 0
        self.peers_disconnected = 0
        self.peers_disconnected_in_row = 0
        self
