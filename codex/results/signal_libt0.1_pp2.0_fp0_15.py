import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl, QTimer, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel

from . import __version__
from . import __author__
from . import __email__
from . import __url__
from . import __license__
from . import __copyright__

from . import __title__
from . import __description__

from . import __appname__
from . import __appauthor__
from . import __appemail__
from . import __appurl__
from . import __applicense__
from . import __appcopyright__

from . import __appname__
from . import __appauthor__
from . import __appemail__
from . import __appurl__
from . import __applicense__
from . import __appcopyright
