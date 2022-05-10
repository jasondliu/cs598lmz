import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# This is the main window of the application
class MainWindow(QtGui.QMainWindow):

    # Constructor function
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('GPS Logger')
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))
        self.resize(800, 600)
        self.center()

        # Create the menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        viewMenu = menubar.addMenu('&View')
        helpMenu = menubar.addMenu('&Help')

        # Add the exit button
        exitButton = QtGui.QAction(QtGui.QIcon('images/exit.png'), '&Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip
