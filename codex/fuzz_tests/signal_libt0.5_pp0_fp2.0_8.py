import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#Qt.QApplication.setGraphicsSystem('raster')
app = Qt.QApplication(sys.argv)
#mw = Qt.QMainWindow()
#mw.resize(800, 800)

scene = QtGui.QGraphicsScene()

#view = QtGui.QGraphicsView(scene)
view = pg.GraphicsLayoutWidget()
#view.setBackground('w')
#view.setRenderHint(QtGui.QPainter.Antialiasing)
#view.show()
#view.setWindowTitle('pyqtgraph example: ImageItem')
#view.resize(600,600)

win = pg.GraphicsLayoutWidget()
win.show()
win.resize(800,800)

#view = pg.GraphicsLayoutWidget()
#view.show()
#view.resize(800,800)

w1 = view.addPlot()
#w1.setWindowTitle('pyqtgraph example: ImageItem')

