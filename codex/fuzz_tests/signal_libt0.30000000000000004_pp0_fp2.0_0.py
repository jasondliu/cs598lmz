import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import __version__
from . import __license__
from . import __copyright__
from . import __author__
from . import __email__
from . import __url__
from . import __description__

from . import mainwindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtPyVCP")
    app.setOrganizationName("QtPyVCP")
    app.setOrganizationDomain("https://github.com/QtPyVCP/QtPyVCP")

    app.setApplicationVersion(__version__)
    app.setWindowIcon(QIcon(":/qtpyvcp_logo.svg"))

    app.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app.setStyle("Fusion")

    # create and show the splash screen
    splash_pix = QPixmap(":/
