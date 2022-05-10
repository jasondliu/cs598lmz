import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the application and set up the main window
app = QApplication(sys.argv)
win = MainWindow()
win.show()

# Run the application
sys.exit(app.exec_())
