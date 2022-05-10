import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create QApplication
app = QApplication(sys.argv)

# Create and show mainWindow
mainWindow = MainWindow()
mainWindow.show()

# Execute application
sys.exit(app.exec_())
