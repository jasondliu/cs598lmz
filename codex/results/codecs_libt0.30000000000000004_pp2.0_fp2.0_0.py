import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_data)
        self.ui.pushButton_2.clicked.connect(self.save_data)
        self.ui.pushButton_3.clicked.connect(self.clear_data)
        self.ui.pushButton_4.clicked.connect(self.open_file)
        self.ui.pushButton_5.clicked.connect(self.save_file)
        self.ui.pushButton_6.clicked.connect(self.open_dir)
        self.ui.pushButton_7.clicked.connect(self.save_dir)
        self.ui.pushButton_8.clicked.
