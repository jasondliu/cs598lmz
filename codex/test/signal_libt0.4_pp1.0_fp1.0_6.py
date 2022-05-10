import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class QtGui(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_file)
        self.ui.pushButton_2.clicked.connect(self.open_file2)
        self.ui.pushButton_3.clicked.connect(self.open_file3)
        self.ui.pushButton_4.clicked.connect(self.open_file4)
        self.ui.pushButton_5.clicked.connect(self.open_file5)
        self.ui.pushButton_6.clicked.connect(self.open_file6)
        self.ui.pushButton_7.clicked.connect(self.open_file7)
        self.ui.pushButton
