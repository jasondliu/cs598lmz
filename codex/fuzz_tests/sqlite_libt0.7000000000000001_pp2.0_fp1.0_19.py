import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import re
import subprocess
import shutil
import signal
import shlex
import math
import traceback
import zipfile

# for pyqt5
import PyQt5

# for pyqt4
#import PyQt4

# for pyside
#import PySide

if sys.version_info[0] == 3:
    from urllib.request import pathname2url
else:
    from urllib import pathname2url

# import PyQt5.QtCore
# import PyQt5.QtGui
# import PyQt5.QtWidgets

# import PyQt4.QtCore
# import PyQt4.QtGui

# import PySide.QtCore
# import PySide.QtGui

# qt5
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets

# qt4
# import PyQt4.QtCore
