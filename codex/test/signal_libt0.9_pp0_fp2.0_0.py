import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)

from PyQt5 import QtWebKitWidgets,QtWebKit,QtWidgets

from PyQt5 import QtCore

import easygui
import threading

class DownloadAction(QtCore.QObject):
    def __init__(self):
        super(DownloadAction,self).__init__()
        self.network = None

    def setNetwork(self,network):
        self.network = network        

    @QtCore.pyqtSlot()
    def download(self):
        print (QtWebKit.QWebPage.DownloadRequested)
        pass

class Win(QtWidgets.QMainWindow):
    def __init__(self):
        super(Win,self).__init__()
        self.setupUi()

    def setupUi(self):
        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)

