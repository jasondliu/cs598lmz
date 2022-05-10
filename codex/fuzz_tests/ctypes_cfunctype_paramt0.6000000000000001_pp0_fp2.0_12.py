import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class MyWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle('PyQt')
        self.setGeometry(50, 50, 600, 600)

        self.button_list = []

        self.button_box = QtGui.QVBoxLayout()
        self.button_box.addStretch(1)

        self.button_list.append(QtGui.QPushButton('Button1'))
        self.button_list.append(QtGui.QPushButton('Button2'))
        self.button_list.append(QtGui.QPushButton('Button3'))

        for button in self.button_list:
            self.button_box.addWidget(button)

        self.setLayout(self.button_box)

        for button in self.button_list:
            button.clicked.connect(self.fun)

    def fun(self):
        print('fun')

