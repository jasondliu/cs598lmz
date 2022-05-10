import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import __version__
from . import __author__
from . import __email__
from . import __license__
