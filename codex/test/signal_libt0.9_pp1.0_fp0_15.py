import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import ctypes

class QTabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        size = QtWidgets.QTabBar.tabSizeHint(self, index)
        size.transpose()
        return size
    
class QLabel2(QtWidgets.QLabel):
    def eventFilter(self, obj, event):
        if event.type()==QtCore.QEvent.MouseButtonPress:
            self.emit(QtCore.SIGNAL('clicked()'))
        return False
    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setMinimumSize(350,350)
        self.tabwidget = QtWidgets.QTabWidget()
        self.tabwidget.setTab
