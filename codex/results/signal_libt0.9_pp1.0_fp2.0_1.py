import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QPushButton")
window.resize(300, 50)
window.show()
app.processEvents()
app.exec_()
import sys
from PySide2.QtWidgets import (QApplication, QPushButton, QListWidget, QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, QObject

class Translator(QObject):
    @Slot()
    def say_hello(self):
        print("Hello World")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QPushButton")
layout = QVBoxLayout()

btn1 = QPushButton("Button 1")
btn2 = QPushButton("Button 2")
layout.addWidget(btn1)
layout.addWidget(btn2)

window.setLayout(layout)

translator = Translator()

#Connect the Signal to
