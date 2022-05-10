import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a Qt application
app = qt.QApplication(sys.argv)

# Create a Button
button = qt.QPushButton("Hello World")
button.show()

# Run the application
sys.exit(app.exec_())
