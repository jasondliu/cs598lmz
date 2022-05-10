import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtGui import QApplication
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

sys.exit(app.exec_())
</code>
And here is mainwindow.py:
<code>import sys
import os
import commands
import subprocess
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

current_path = sys.argv[0]
current_directory = os.path.dirname(current_path)

MainWindow_pgd = os.path.join(current_directory, 'MainWindow.ui')

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

   
