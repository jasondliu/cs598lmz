import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a QApplication with the command line arguments
app = QApplication(sys.argv)

# Create a main window
w = QMainWindow()
w.setWindowTitle('QMainWindow')
w.resize(800, 600)

# Create a button in the window
button = QPushButton('Press me!')
w.setCentralWidget(button)


def on_button_clicked():
    print('Button clicked!')


# Connect the button to the on_button_clicked function
button.clicked.connect(on_button_clicked)

# Show the main window and run the qt application
w.show()
app.exec_()
