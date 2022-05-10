import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('搜索文件')
        self.resize(800, 600)
        self.status = self.statusBar()
        self.status.showMessage('准备就绪', 5000)
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.textEdit.setFocus()

        self.createAction()
        self.createMenu()
        self.createToolBar()

    def createAction(self):
        self.openFileAction = QAction(QIcon('./images/open.png'), '打开', self)
        self.openFileAction.setShortcut('Ctrl+O')
        self
