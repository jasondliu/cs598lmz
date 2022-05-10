import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# This should be done early in the process to force a proxy setting
import JOCR_Settings as JOCR
JOCR.get_setting("proxy_cl_app")

# Import application
from gui.MainWindow import MainWindow

# We need this to make pickle work
import gui.MainWindow

# Create the QApplication
app = QtGui.QApplication(sys.argv)

# Create and show the window
w = MainWindow()
w.show()

# Execute application
sys.exit(app.exec_())
