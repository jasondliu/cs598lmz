import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the Qt Application
app = QtGui.QApplication(sys.argv)

# Create and show the splash screen
splash_pix = QtGui.QPixmap('/home/gabor/Dokumentumok/Python/Experiment_Program/splash.jpg')
splash_pix = splash_pix.scaledToHeight(480)
splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
splash.setWindowFlags(QtCore.Qt.FramelessWindowHint)
splash.show()
app.processEvents()

# Construct our Qt App, hide the main window
# and execute the reactor in another thread
w = MainWindow()
w.hide()
reactor.callInThread(reactor.run)

# ...zm1, zm2 and zm3 are AFM-s parameters...
