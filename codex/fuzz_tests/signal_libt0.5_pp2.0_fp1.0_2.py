import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

from ui.mainwindow import MainWindow

app = QtGui.QApplication(sys.argv)

w = MainWindow()
w.show()

sys.exit(app.exec_())
