import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from ui_mainwindow import Ui_MainWindow

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect up the buttons
        QtCore.QObject.connect(self.ui.btnQuit,QtCore.SIGNAL("clicked()"),self.btnQuit_clicked)
        QtCore.QObject.connect(self.ui.btnHello,QtCore.SIGNAL("clicked()"),self.btnHello_clicked)

    def btnHello_clicked(self):
        self.ui.lblResponse.setText("Hello World!")

