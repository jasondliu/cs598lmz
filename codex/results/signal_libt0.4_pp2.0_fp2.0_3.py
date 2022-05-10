import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Initialize the Qt application
app = QApplication(sys.argv)

# Create the main window and set its title
win = QMainWindow()
win.setWindowTitle('PyQt4 example')

# Create a button in the main window and connect it to the on_click function
button = QPushButton('Click me', win)
button.clicked.connect(on_click)

# Create a QLabel widget with a welcome message
label = QLabel('<h1>Welcome to the PyQt4 example</h1>', win)

# Create a vertical box layout and add the label and button to it
vbox = QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(button)

# Create a QWidget and set the layout
widget = QWidget()
widget.setLayout(vbox)

# Set the central widget of the Window
win.setCentralWidget(widget)

# Show the main window and start the Qt main loop execution, exiting from this
