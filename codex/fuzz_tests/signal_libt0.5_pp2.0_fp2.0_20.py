import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.open_file)
        self.ui.pushButton_2.clicked.connect(self.save_file)
        self.ui.pushButton_3.clicked.connect(self.exit)

        self.ui.pushButton_4.clicked.connect(self.add_row)
        self.ui.pushButton_5.clicked.connect(self.remove_row)
        self.ui.pushButton_6.clicked.connect(self.add_column)
        self.ui.pushButton_7.clicked.connect(self.remove_column)

        self.ui.pushButton_8.clicked.connect(self.set_background_color)
