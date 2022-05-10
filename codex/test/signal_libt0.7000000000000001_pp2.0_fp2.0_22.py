import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui

from main import Main

class PyDiggerGui(QtGui.QApplication):
    def __init__(self, argv):
        QtGui.QApplication.__init__(self, argv)
        self.main = Main()
        self.main.show()

if __name__ == '__main__':
    app = PyDiggerGui(sys.argv)
    app.exec_()
