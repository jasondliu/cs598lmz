import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("MainWindow")
        self.setMinimumSize(QtCore.QSize(200, 100))

        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        button = QtWidgets.QPushButton("Show Dialog", clicked=self.show_dialog)
        layout.addWidget(button)

    def show_dialog(self):
        dlg = Dialog(self)
        dlg.exec_()

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setWindowTitle("
