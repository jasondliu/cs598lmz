import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('My App')

        self.tray_icon = QtGui.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtGui.QStyle.SP_ComputerIcon))
        show_action = QtGui.QAction("Show", self)
        quit_action = QtGui.QAction("Exit", self)
        hide_action = QtGui.QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(self.close)
        tray_menu = QtGui.QMenu()
        tray_menu.addAction(
