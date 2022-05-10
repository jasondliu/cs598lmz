import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from .mainwindow import MainWindow
from . import __version__

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtPyVCP")
    app.setApplicationVersion(__version__)
    app.setOrganizationName("QtPyVCP")
    app.setOrganizationDomain("qtpyvcp.org")
    app.setWindowIcon(QIcon(":/qtpyvcp/images/qtpyvcp_icon.png"))

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
