import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a GUI window
app = QtGui.QApplication(sys.argv)

# Create and display the splash screen
splash_pix = QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'gui', 'splash.png'))
splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
splash.setMask(splash_pix.mask())
splash.show()
app.processEvents()

# Import the main window
from gui.main_window import MainWindow

# Create the main window
main_window = MainWindow()
main_window.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'gui', 'icon.png')))

# Close the splash screen
splash.finish(main_window)

# Display the window
main_
