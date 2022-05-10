import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# main
if __name__ == '__main__':
    # メインウインドウ
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
