import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a new instance of the App class
app = App()

# Create a new instance of the MainWindow class
main_window = MainWindow()

# Show the main window
main_window.show()

# Run the application
app.exec_()
