import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from ui_main import Ui_MainWindow

# Import the code for the dialog
from dialog_about import AboutDialog

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect the buttons to functions
        self.ui.btnQuit.clicked.connect(self.quit)
        self.ui.btnAbout.clicked.connect(self.about)

    def about(self):
        # Create the dialog (after translation) and keep reference
        self.about = AboutDialog()
        self.about.show()
        
