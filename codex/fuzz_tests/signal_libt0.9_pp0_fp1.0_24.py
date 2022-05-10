import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(150, 150)
        self.setWindowTitle('Bounce')

        self.file_menu = QtGui.QMenu('&File', self)
        self.menuBar().addMenu(self.file_menu)
        self.exit_action = self.file_menu.addAction('&Quit')
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Exit application')
        self.exit_action.triggered.connect(self.close)

        self.statusBar().showMessage("Ready")
        self.centralwidget = QtGui.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.bounce = Bounce(self.centralwidget)
        self.bounce.start()

        self.
