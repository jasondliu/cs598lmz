import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QDockWidget, QFileDialog
from PyQt4.QtCore import QThread, SIGNAL
from PyQt4.Qt import QString
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import QStringList
from PyQt4.QtCore import QStringListModel
from PyQt4.QtCore import QModelIndex
from PyQt4.QtCore import QObject
from PyQt4.QtCore import QEvent
from PyQt4.QtCore import QProcess
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QIcon
from PyQt4.Q
