import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Taskbar Example')
        self.setWindowIcon(QIcon('lena.jpg'))

        self.text = QLabel('Hello, world!')

        self.btn = QPushButton('Quit')
        self.btn.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
   
