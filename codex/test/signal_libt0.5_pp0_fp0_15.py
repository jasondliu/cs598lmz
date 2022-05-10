import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, QUrl, pyqtSlot, pyqtSignal
from PyQt5.QtQml import QQmlApplicationEngine


class Bridge(QObject):
    '''
    Class to expose the model to QML
    '''

    # create a signal to be used from Python to communicate with QML
    updateStatus = pyqtSignal(str)

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        # create a timer to update the model in regular intervals
        self.timer = QTimer()
        self.timer.timeout.connect(self._update)
        self.timer.start(1000)
        self.i = 0

    @pyqtSlot(str)
    def printToConsole(self, msg):
        '''
        Slot to demonstrate how to interact with QML from Python
        '''
