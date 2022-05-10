import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Simple')
w.show()
sys.exit(app.exec_())
