import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Create the main window
class MainWindow(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("This is a PyQt5 window!")
        btn = QtWidgets.QPushButton("Click me!")

        btn.pressed.connect(self.magic)

        layout.addWidget(self.label)
        layout.addWidget(btn)

        self.setLayout(layout)

    def magic(self):
        self.label.setText("You clicked the button!")


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()
