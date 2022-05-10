import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Set up the main window
win = MainWindow()
win.show()

# Start the Qt event loop
app.exec_()
