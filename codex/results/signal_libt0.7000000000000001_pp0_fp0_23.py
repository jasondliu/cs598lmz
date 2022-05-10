import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

"""
Main Window
"""
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Qt5 UI")
        self.resize(900, 600)
        self.setWindowIcon(QIcon("icon.png"))

        # central widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # layout
        self.layout = QVBoxLayout(self.centralWidget)

        # buttons
        self.btn_start = QPushButton("START")
        self.btn_stop = QPushButton("STOP")
        self.btn_reset = QPushButton("RESET")

        # buttons layout
        self.layout_buttons = QHBoxLayout()
        self.layout_buttons.addWidget(self.btn_start)
        self.layout_buttons.addWidget(self.btn_stop)
        self.layout_
