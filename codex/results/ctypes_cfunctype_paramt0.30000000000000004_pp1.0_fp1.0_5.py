import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('MyWindow')
        self.setGeometry(100,100,100,100)
        self.button = QtGui.QPushButton('Click me', self)
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print 'button clicked'

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
</code>

