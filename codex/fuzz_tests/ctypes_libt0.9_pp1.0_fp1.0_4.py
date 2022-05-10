import ctypes
ctypes.windll.user32.MessageBoxW(0, "Yoyoyoyo bro!", "Your title", 1)

'''
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
class Ui(QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.my_function)
    def my_function(self):
        QMessageBox.information(QMessageBox(), 'Alert', 'The application will now quit', QMessageBox.Ok)
        app.quit()

app = QApplication([])
window = Ui()
window.setWindowTitle('MyWindow')
window.base.setWindowTitle('MyWindow')
window.show()
app.exec_()
