import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import config
from . import mainwindow
from . import util

def main():
    # initialize application
    app = QApplication(sys.argv)
    app.setApplicationName(config.APP_NAME)
    app.setOrganizationName(config.ORG_NAME)

    # initialize main window
    window = mainwindow.MainWindow()
    window.show()

    # run application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
