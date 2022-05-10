import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("Qt5 Application")

# Create the main widget
widget = QWidget()
widget.setLayout(QVBoxLayout())
window.setCentralWidget(widget)

# Create the label
label = QLabel("Hello World")
widget.layout().addWidget(label)

# Create the button
button = QPushButton("Click me")
widget.layout().addWidget(button)

# Show the window
window.show()

# Run the application
app.exec_()
</code>

