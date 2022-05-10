import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.pushButton_4.clicked.connect(self.pushButton_4_clicked)
        self.pushButton_6.clicked.connect(self.pushButton_6_clicked)
        self.pushButton_7.clicked.connect(self.pushButton_7_clicked)
        self.pushButton_9.clicked.connect(self.pushButton_9_clicked)
        self.
