import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import argparse
import logging
import logging.handlers
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets

from . import __version__
from . import __description__
from . import __url__
from . import __license__
from . import __copyright__
from . import __author__
from . import __email__
from . import __appname__
from . import __appname_lower__
from . import __appname_upper__
from . import __appname_title__
from . import __appname_upper_no_space__
from . import __appname_lower_no_space__
from . import __appname_upper_no_space_no_dash__
from . import __appname_lower_no_space_no_dash__
from . import __appname_upper_no_space_no_dash_no_dot__
from . import __appname_lower_no_space_no
