import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Load QtApp
from PyQt4.QtGui import QApplication

# Load Scripts
import mainwindow
