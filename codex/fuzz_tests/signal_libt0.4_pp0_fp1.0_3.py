import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create an instance of the application class
app = QApplication(sys.argv)

# Create and show the main window
main_window = MainWindow()
main_window.show()

# Start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
