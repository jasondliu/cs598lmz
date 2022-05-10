import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Main window
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Lattice QCD Spectroscopy')
        self.setGeometry(0, 0, 800, 600)
        self.central_widget = QtGui.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtGui.QHBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.central_widget.setLayout(self.layout)

        self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.layout.addWidget(self.splitter)

        self.left_widget = QtGui.QWidget()
        self.left_layout = QtGui.
