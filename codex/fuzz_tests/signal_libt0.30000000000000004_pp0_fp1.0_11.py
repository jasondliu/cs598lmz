import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QCoreApplication, QObject, pyqtSlot, QUrl
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication

#from PyQt5.QtCore import QObject, pyqtSlot, QUrl
#from PyQt5.QtQml import QQmlApplicationEngine
#from PyQt5.QtGui import QGuiApplication
#from PyQt5.QtQuick import QQuickView
#from PyQt5.QtWidgets import QApplication

class Backend(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.count = 0

    @pyqtSlot()
    def doAction(self):
        self.count += 1
