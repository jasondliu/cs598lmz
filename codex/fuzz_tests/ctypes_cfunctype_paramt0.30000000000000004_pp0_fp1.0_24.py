import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('QtGui.QSystemTrayIcon')
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(u'Показать', self.showNormal)
        self.trayIconMenu.addAction(u'Закрыть', self.close)
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.setIcon(QtGui.QIcon('tray.png'))
        self.trayIcon.show()
        self.trayIcon.messageClicked.connect(self.messageClicked)
        self.tr
