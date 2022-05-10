import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from .main_window import MainWindow
from . import config

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName(config.ORGANIZATION_NAME)
