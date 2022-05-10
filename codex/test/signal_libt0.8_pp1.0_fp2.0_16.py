import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication

def main():
    import sys
    app = QApplication(sys.argv)
    app.setOrganizationName('linusdt')
    app.setApplicationName('fakenet')
    app.setOrganizationDomain('com.fakenet')

    # setup splash screen
    from PyQt5.QtWidgets import QSplashScreen
    from PyQt5.QtGui import QPixmap
    import os
    splash_pix = QPixmap(os.path.join(os.path.dirname(__file__), 'fakenet_logo.svg'))
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()

    # setup main window
    import settings
    settings.load()
