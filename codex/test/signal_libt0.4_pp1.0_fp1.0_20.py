import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
