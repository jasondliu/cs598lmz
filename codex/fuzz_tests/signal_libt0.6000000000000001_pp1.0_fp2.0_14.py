import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self) 
        self.setCentralWidget(self.form_widget)

class FormWidget(QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.pushButton = QPushButton("Push Me")
        self.pushButton.clicked.connect(self.button_clicked)
        self.layout.addWidget(self.pushButton)

    def button_clicked(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog")
        dialog.setLayout(QVBoxLayout())
        dialog.layout().addWidget(QLabel("Hello"))
        dialog.show()

if
