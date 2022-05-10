import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) 



class MainWindow (QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.title = 'VISUAL MANAGEMENT SYSTEM'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 400
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar()

        menu = self.menuBar()
        fileMenu = menu.addMenu("&File")
        fileMenu.addAction("New")
        fileMenu.addAction("Open")
        fileMenu.addAction("Save")
        fileMenu.addAction("Save AS")
        fileMenu.addAction("Exit")

        viewMenu = menu.addMenu("&View")
        viewMenu.addAction("Show StatusBar")
