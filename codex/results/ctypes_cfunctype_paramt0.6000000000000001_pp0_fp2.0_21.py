import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.pushButton = QtGui.QPushButton("Push me")
        self.button = self.createButton('Test', self.customContextMenuRequested)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.textEdit = QtGui.QTextEdit()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self, QtCore.SIGNAL('customContextMenuRequested(QPoint)'), self.contextMenuRequested)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.button)
        layout.addWidget(self.textEdit)

    def
