import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from . import __version__
from .ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("pyPhyloMaker")
    app.setOrganizationName("pyPhyloMaker")
    app.setOrganizationDomain("pyphylomaker.github.io")
    app.setApplicationVersion(__version__)
    app.setWindowIcon(QIcon(":/icons/pyphylomaker.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
