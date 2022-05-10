import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QVariant, QTimer, QThread
from PyQt5.QtDBus import QDBusConnection, QDBusMessage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QJSValue

app = QApplication([])

class App(QObject):

    def __init__(self):
        super().__init__()
        # QDBusConnection.sessionBus().registerService("org.kde.plasmashell")
        QDBusConnection.sessionBus().registerService("org.kde.plasmashell")
        QDBusConnection.sessionBus().registerObject("/MainApplication", self, QDBusConnection.ExportScriptableSlots)
        self.processes = []

    testSlot = pyqtSignal(QVariant)

    @pyqtSlot('QVariant', result='QVariant')
    def
