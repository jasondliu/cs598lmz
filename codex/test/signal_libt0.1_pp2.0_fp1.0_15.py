import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import mainwindow

def main():
    app = QApplication(sys.argv)
    window = mainwindow.MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
