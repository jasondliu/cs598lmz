import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Josiah Bryan")
    app.setOrganizationDomain("josiahbryan.com")
    app.setApplicationName("XBMC Remote")
    app.setWindowIcon(QIcon(":/icons/xbmc-remote.png"))

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
