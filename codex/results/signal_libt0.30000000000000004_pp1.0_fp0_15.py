import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.stop)
        self.ui.pushButton_3.clicked.connect(self.exit)
        self.ui.pushButton_4.clicked.connect(self.clear)
        self.ui.pushButton_5.clicked.connect(self.save)
        self.ui.pushButton_6.clicked.connect(self.load)
        self.ui.pushButton_7.clicked.connect(self.show_help)
        self.ui.pushButton_8.clicked.connect(self.show_about)
        self.ui.pushButton_9.cl
