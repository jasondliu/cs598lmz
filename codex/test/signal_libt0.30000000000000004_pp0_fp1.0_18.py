import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

