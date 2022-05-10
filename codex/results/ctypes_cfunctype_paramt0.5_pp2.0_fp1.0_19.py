import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class App(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setWindowTitle('Test')
        self.resize(300, 100)

        self.button = QtWidgets.QPushButton('Test', self)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        print('Button clicked')
        print('Calling the callback')
        self.callback()

    def set_callback(self, callback):
        self.callback = FUNTYPE(callback)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    def callback():
        print('Callback called')

    window = App()
    window.set_callback(callback)
    window.show()

    sys.exit(app.exec_())
</code>

