import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a Qt application
app = QApplication(sys.argv)

# Create a Window
win = QMainWindow()
win.setWindowTitle('PyQt5 GUI')

# Create a widget
label = QLabel('Hello World!')
label.setAlignment(Qt.AlignCenter)

# Set the central widget of the Window. Widget will expand
# to take up all the space in the window by default.
win.setCentralWidget(label)

# Show the window and run the app
win.show()
app.exec_()
