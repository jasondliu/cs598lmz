import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
# It's exec_ because exec is a reserved word in Python
