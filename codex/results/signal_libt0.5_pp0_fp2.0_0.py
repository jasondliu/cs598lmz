import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import util
from . import mainwindow
from . import terminal

def main():
    util.init_logging()
    app = QApplication(sys.argv)
    window = mainwindow.MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
