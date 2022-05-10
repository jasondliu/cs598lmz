import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QSystemTrayIcon

from . import __version__
from . import __copyright__
from . import __license__
from . import __author__
from . import __email__
from . import __url__
from . import __appname__
from . import __appname_lower__
from . import __appname_upper__
from . import __appname_title__
from . import __appname_version__
from . import __appname_version_str__
from . import __appname_full__

from . import __qt_version__
from . import __qt_version_str__

from . import __pyqt_version__
from . import __pyqt_version_str__

from . import __sip_version__
from . import __sip_version_
