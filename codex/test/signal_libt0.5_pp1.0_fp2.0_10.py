import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(1000, 600)
        self.setWindowTitle('Crazyflie Client')

        # Create the status bar
        self.statusBar().showMessage('Disconnected')

        # Create a menu bar
        self.createMenu()

    def createMenu(self):
        # File menu
        fileMenu = self.menuBar().addMenu("&File")
        exitAction = fileMenu.addAction("&Exit")
        exitAction.triggered.connect(self.close)

        # Help menu
        helpMenu = self.menuBar().addMenu("&Help")
        aboutAction = helpMenu.addAction("&About")
        aboutAction.triggered.connect(self.about)

