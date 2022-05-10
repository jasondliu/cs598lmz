import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QApplication(sys.argv)

# Create and display the splash screen
splash_pix = QPixmap('splash_tangram.png')
splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
splash.setMask(splash_pix.mask())
splash.show()
splash.showMessage("<h1><font color='white'>Welcome to Tangram!</font></h1>",
                   Qt.AlignBottom | Qt.AlignCenter, Qt.black)
app.processEvents()

# Simulate something that takes time
time.sleep(1)

# Create and display the main window
window = Window()
window.show()

# Close the splash screen
splash.finish(window)

# Execute the application
