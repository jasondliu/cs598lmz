import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

sys.path.append(PyQt5.uic.uipath)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from fbs_runtime.application_context.PyQt5 import ApplicationContext

class About(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.ui = uic.loadUi("About.ui", self)
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)

        self.setWindowTitle("About")
        self.show()

    def pushButton_clicked(self):
        self.close()

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def __init__(self):
        super().__init__()
        self.about = About()

        #self.window = MainWindow(
