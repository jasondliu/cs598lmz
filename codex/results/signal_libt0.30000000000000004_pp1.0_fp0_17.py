import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import __version__
from . import __author__
from . import __email__
from . import __license__
from . import __copyright__
from . import __url__

from .mainwindow import MainWindow
from . import config
from . import log
from . import utils

def main():
    """
    Main function
    """
    # Parse arguments
    parser = argparse.ArgumentParser(description="Qt5 port of the Pymol molecular visualization system.")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s " + __version__)
    parser.add_argument("-c", "--config", help="Path to the configuration file.")
    parser.add_argument("-l", "--log", help="Path to the log file.")
    parser.add_argument("-d", "--debug", help="Enable debug mode.", action="store_
