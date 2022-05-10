import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

from . import __version__
from . import __author__
from . import __email__
from . import __url__
from . import __license__

from . import __appname__
from . import __description__
from . import __copyright__

from . import __appname_lower__
from . import __appname_upper__

from . import __shortname__
from . import __shortname_lower__
from . import __shortname_upper__

from . import __appname_full__
from . import __appname_full_lower__
from . import __appname_full_upper__

from . import __shortname_full__
from . import __shortname_full_lower__
from . import __shortname_full_upper__

from . import __appname_full_short__
