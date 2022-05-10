import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a Qt application
app = QApplication(sys.argv)

# Create the main window
w = QMainWindow()
w.setWindowTitle("Simple example")

# Create a button in the window
btn = QPushButton('Press Me', w)
btn.setToolTip('Press to quit!')
btn.resize(btn.sizeHint())
btn.move(50, 50)

# Create the actions
@pyqtSlot()
def on_click():
    print('PyQt5 button click')

# connect the signals to the slots
btn.clicked.connect(on_click)

# Show the window and run the app
w.show()
app.exec_()
