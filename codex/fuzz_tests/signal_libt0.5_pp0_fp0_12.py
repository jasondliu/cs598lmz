import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a QApplication instance
app = QApplication(sys.argv)

# Create and show the main window
window = MainWindow()
window.show()

# Execute the application
app.exec_()
