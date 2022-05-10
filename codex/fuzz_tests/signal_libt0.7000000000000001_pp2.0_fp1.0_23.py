import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        self.setWindowTitle('PyQt')

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

app = QtGui.QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
</code>

