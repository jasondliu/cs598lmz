import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# ...

# Import QT modules
from PyQt4 import QtGui, QtCore

# Import the compiled UI module
import ui_mainwindow

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

# Create the Qt Application
app = QtGui.QApplication(sys.argv)

# Create and show the form
form = MainWindow()
form.show()

# Run the main Qt loop
sys.exit(app.exec_())
</code>

