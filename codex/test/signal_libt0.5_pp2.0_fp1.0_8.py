import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(1000, 800)
        self.setWindowTitle('QtGui.QGraphicsView')

        self.scene = QtGui.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1000, 800)
        self.view = QtGui.QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.add_items()

        self.show()

    def add_items(self):
        self.scene.addLine(0, 0, 100, 100)
        self.scene.addLine(100, 0, 0, 100)

        rect = QtCore.QRectF(0, 0, 100, 100)
        rect_item = QtGui.QGraphicsRectItem(rect)
