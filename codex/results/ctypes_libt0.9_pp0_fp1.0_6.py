import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import PyQt5.QtWidgets
import PyQt5.QtCore

class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CASABiA")
        self.tab = PyQt5.QtWidgets.QTabWidget()
        self.tab.addTab(PyQt5.QtWidgets.QWidget(self.tab), "My Tab")
        self.setCentralWidget(self.tab)
    
    def update(self):
        path = "C:/Users/Gebruiker/Desktop/test"
        for file in os.listdir(path):
            if file.endswith(".png"):
                
                button = PyQt5.QtWidgets.QPushButton(os.path.splitext(file)[0])
                
                button.
