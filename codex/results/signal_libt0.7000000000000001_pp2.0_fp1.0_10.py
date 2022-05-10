import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_ui()

    def setup_window(self):
        self.resize(800, 600)
        self.move(300, 300)
        self.setWindowTitle('Pliki i foldery')

    def setup_ui(self):
        # central widget as a placeholder
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # main layout
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        # basic data
        self.name = QLineEdit()
        self.path = QLineEdit()
        self.path.setReadOnly(True)
        self.type = QLineEdit()
        self.type.setReadOnly(True)
        self.size = QLineEdit()
        self
