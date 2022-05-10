import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
