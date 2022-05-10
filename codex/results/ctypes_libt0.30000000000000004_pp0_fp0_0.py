import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QtWidgets.QLabel("THIS IS AWESOME!!!")
        label.setAlignment(QtCore.Qt.AlignCenter)

        self.setCentralWidget(label)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
</code>

