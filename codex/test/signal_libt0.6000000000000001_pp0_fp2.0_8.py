import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

