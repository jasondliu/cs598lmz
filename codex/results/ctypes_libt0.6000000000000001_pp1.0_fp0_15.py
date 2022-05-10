import ctypes
ctypes.windll.user32.MessageBoxW(None, 'Hello World!', 'Hello Dialog', 0)
</code>
However, I am not sure how to get the MessageBox to pop up right after the user clicks on a button. 


A:

You can use PyQt5 <code>QMessageBox</code> like this:
<code>from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Message Box"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        button = QPushButton("Click Me", self)
        button.move(200, 100)
        button.clicked.connect(self.clickMe)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.
