import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
