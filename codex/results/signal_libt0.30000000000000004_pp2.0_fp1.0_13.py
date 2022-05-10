import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from . import __version__
from . import __description__
from . import __author__
from . import __author_email__
from . import __license__
from . import __url__
from . import __copyright__
from . import __appname__
from . import __appname_lower__
from . import __appname_upper__
from . import __appname_title__
from . import __appname_upper_title__
from . import __appname_lower_title__
from . import __appname_upper_title_spaced__
from . import __appname_lower_title_spaced__
from . import __appname_upper_camel__
from . import __appname_lower_camel__
from . import __appname_upper_camel_spaced
