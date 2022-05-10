import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

mainwindow.setWindowTitle("Pepper")
mainwindow.setWindowIcon(QtGui.QIcon('Logo.png'))

if __name__ == '__main__':
    sys.exit(app.exec_())
