import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class QQ(QMainWindow):

    def __init__(self):
        super(QQ, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def QQ_show(self):
        # os.system('taskkill /F /IM devtools.exe')
        # os.system('taskkill /F /IM qq.exe')
        app = QApplication(sys.argv)
        window = QQ()
        window.show()
        sys.exit(app.exec_())
