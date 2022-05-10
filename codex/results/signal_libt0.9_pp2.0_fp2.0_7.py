import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

# Fill the namespace with all QObject descendants, for convenience.
# Note that all of which are in fact exported by Qt5. This does not
# mean that PySide2 offers bindings for all of which.

QObject.__subclasses__()
