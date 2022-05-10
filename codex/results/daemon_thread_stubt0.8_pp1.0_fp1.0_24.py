import sys, threading

def run():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle("Image Show")
    w.setWindowIcon(QtGui.QIcon('lenna.jpg'))
    w.setGeometry(40, 40, 600, 400)
    label = QtWidgets.QLabel(w)
    pixmap = QtGui.QPixmap('lenna.jpg')
    label.setPixmap(pixmap)
    w.show()
    sys.exit(app.exec())

threading.Thread(target=run).start()
