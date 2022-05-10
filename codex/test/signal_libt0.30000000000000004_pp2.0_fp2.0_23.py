import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a new instance of the QtGui.QApplication class
app = QtGui.QApplication(sys.argv)

# Create the main window
window = QtGui.QMainWindow()

# Set some main window's properties
window.setWindowTitle("PyQt")
window.setMinimumSize(400, 400)

# Create a vertical layout
layout = QtGui.QVBoxLayout()

# Create a horizontal layout
hlayout = QtGui.QHBoxLayout()

# Create a label
label = QtGui.QLabel("This is a label")

# Create a line edit
line_edit = QtGui.QLineEdit()

# Create a push button
button = QtGui.QPushButton("Click me!")

# Add the label to the vertical layout
layout.addWidget(label)

# Add the line edit to the vertical layout
layout.addWidget(line_edit)

# Add the button to the horizontal layout
