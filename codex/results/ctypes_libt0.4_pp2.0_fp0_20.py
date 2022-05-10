import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Create the application
app = QtWidgets.QApplication(sys.argv)

# Create a label and set its properties
label = QtWidgets.QLabel("Hello World!")
label.setAlignment(QtCore.Qt.AlignCenter)

# Create a window and set its properties
window = QtWidgets.QWidget()
window.setWindowTitle("PyQt5 Lesson 1")
window.setGeometry(100,100,280,80)

# Add the label to the window
window.setCentralWidget(label)

# Show the constructed PyQt window
window.show()

# Run the application and clean up
app.exec_()
del label
del window
del app
