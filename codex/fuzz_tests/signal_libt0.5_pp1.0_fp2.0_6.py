import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui
from PyQt4.QtCore import QSettings

from . import __version__
from . import __appname__

from .gui import MainWindow
from .gui.splash import SplashScreen
from .gui.utils import get_icon

def main():
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName("pyzo")
    app.setApplicationName(__appname__)
    app.setApplicationVersion(__version__)
    app.setWindowIcon(get_icon('pyzo.svg'))
    #app.setStyle("plastique")
    
    # Init settings
    settings = QSettings()
    
    # Create splash
    splash = SplashScreen(app)
    splash.show()
    app.processEvents()
    
    # Create main window
    main = MainWindow(app, splash, settings)
    main.show()
    main.raise_()
    
