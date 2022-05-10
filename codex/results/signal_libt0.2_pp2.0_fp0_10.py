import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the application
app = QApplication(sys.argv)

# Create and show the main window
window = MainWindow()
window.show()

# Run the main Qt loop
sys.exit(app.exec_())
