import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
