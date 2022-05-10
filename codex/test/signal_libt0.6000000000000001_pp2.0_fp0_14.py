import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)

        self.ui.pushButton_2.clicked.connect(self.stop)
        self.ui.pushButton_3.clicked.connect(self.show_about)

        self.ui.comboBox.currentIndexChanged.connect(self.change_interface)
        self.ui.comboBox_2.currentIndexChanged.connect(self.change_interface)
        self.ui.comboBox_3.currentIndexChanged.connect(self.change_interface)

