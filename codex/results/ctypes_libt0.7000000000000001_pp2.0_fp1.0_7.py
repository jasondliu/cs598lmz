import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# load the .ui file
Ui_MainWindow, QtBaseClass = uic.loadUiType("MainWindow.ui")



# create a class for our main window
class Window(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # setup the main ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # setup the tray icon
        self.createTrayIcon()

        # setup the window icon
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        # setup the menu actions
        self.setupMenuActions()

        # setup the window actions
        self.setupWindowActions()

        # setup the timer
        self.setupTimer()

        # setup the window position
        self.loadWindowPosition()

        # connect the event
        self.ui.button.clicked.connect(
