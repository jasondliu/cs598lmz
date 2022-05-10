import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a QApplication with the command line arguments
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("PyQtGraph example: PlotWidget")

# Create a PlotWidget
plot = PlotWidget()

# Add it to the window
window.setCentralWidget(plot)

# Show the window
window.show()

# Start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
