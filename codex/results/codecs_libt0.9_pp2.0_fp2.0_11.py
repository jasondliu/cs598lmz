import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class Qrcode(QMainWindow):

    def __init__(self):
        super(Qrcode,self).__init__()
        self.initUi()

    def initUi(self):
        exitAction = QAction('&退出',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出应用程序')
        exitAction.triggered.connect(qApp.quit)

        #状态栏
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAction)
        self.resize(300,250)
        self.setMinimumSize(350,350)
        self.setWindowTitle('QRCode')
        self.setWindowIcon(QIcon('logo.ico'))
