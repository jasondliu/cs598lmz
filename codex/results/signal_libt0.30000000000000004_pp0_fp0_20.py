import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a new instance of the QtGui.QApplication class
app = QtGui.QApplication(sys.argv)

# Create the main window
w = QtGui.QWidget()

# Set window size.
w.resize(320, 240)

# Set window title
w.setWindowTitle("Hello, World!")

# Show window
w.show()

# Run the main Qt loop
sys.exit(app.exec_())
</code>

