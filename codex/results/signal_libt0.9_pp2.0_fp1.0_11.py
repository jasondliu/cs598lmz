import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtGui.QMainWindow):

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left:
            self.hlayout_val = self.hlayout_val - 1
        elif event.key() == QtCore.Qt.Key_Right:
            self.hlayout_val = self.hlayout_val + 1
        elif event.key() == QtCore.Qt.Key_Up:
            self.vlayout_val = self.vlayout_val - 1
        elif event.key() == QtCore.Qt.Key_Down:
            self.vlayout_val = self.vlayout_val + 1
        elif event.key() == QtCore.Qt.Key_1:
            self.layout.setRowStretch(0, self.vlayout_val)
            self.layout.setRowStretch(1, self.vlayout_val)
            self.layout.setColumnStretch(
