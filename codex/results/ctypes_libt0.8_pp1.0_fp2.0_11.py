import ctypes
ctypes.windll.user32.MessageBoxW(0, "Pressed Left-Control + W", "Hi", 1)
</code>
I would like to, instead of having the ctypes library, use pyqt, but how do I do this?
I know how to create a GUI, but how do I make it run in the background and when the user presses the keyboard button, it will pop up the window?


A:

To run a program continuously in the background (such as waiting for a keyboard event) you can use a <code>QApplication</code> with a <code>QTimer</code>.
The following snippet will print every second "hello"
<code>from PyQt4 import QtGui
import sys

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

    def do_something(self):
        print("hello")

    def run(self):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.do_something)
        timer.start(1000) # milliseconds

