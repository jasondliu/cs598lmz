import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

# Create an PyQT5 application object.
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt5.
w = QWidget()

# Set window size.
w.setFixedSize(320, 140)

# Set window title
w.setWindowTitle("PyQt5 Hello World - pythonprogramminglanguage.com")

# Create QLabel
l1 = QLabel()
l1.setText("Hello World")
l1.setAlignment(Qt
