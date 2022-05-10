import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# The main window
class MainWindow(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.setWindowTitle("Hello World!")
        self.setWindowIcon(QIcon("icon.png"))
        self.setMinimumSize(QSize(800, 600))
        
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        
        # Layout
        layout = QVBoxLayout(centralWidget)
        
        # Menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        
        # Actions
        exitAction = QAction(QIcon("exit.png"), "E&xit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(self.close)
        
