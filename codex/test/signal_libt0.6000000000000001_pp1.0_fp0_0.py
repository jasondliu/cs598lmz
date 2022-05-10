import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)



class Image_Viewer(QtGui.QWidget):

    def __init__(self):
        super(Image_Viewer, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Image Viewer')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):

        qp.setPen(QtCore.Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)
