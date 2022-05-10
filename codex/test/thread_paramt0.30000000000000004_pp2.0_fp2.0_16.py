import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Import the core and GUI elements of Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Every PyQt5 application must create an application object.
# The application object is located in the QtWidgets module.
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt5.
# We provide the default constructor for QWidget. The default constructor has no parent.
# A widget with no parent is called a window.
w = QWidget()

# Set window size.
w.resize(320, 240)

# Move window to center of the screen.
w.move(300, 300)

# Set window title
w.setWindowTitle("Hello World!")

# Show window
w.show()

# The mainloop of the application. The event handling starts from this point.
