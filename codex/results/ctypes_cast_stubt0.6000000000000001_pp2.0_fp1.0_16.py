import ctypes
ctypes.cast(0, ctypes.py_object).value = None
# Use the debug version of sip (if installed)
if os.environ.get('QT_DEBUG', '') != '':
    import sip
    sip.setapi('QString', 2)
    sip.setapi('QVariant', 2)
    sip.setapi('QDate', 2)
    sip.setapi('QDateTime', 2)
    sip.setapi('QTextStream', 2)
    sip.setapi('QTime', 2)
    sip.setapi('QUrl', 2)
    sip.setapi('QTextCodec', 2)

# We are also using the debug version of Qt
os.environ['QT_DEBUG'] = '1'

# Import PyQt modules
from PyQt4 import QtCore, QtGui

# Always use the same input method on X11
os.environ['QT_IM_MODULE'] = 'xim'

# Import the compiled UI module
from gui.ui_mainwindow import Ui_MainWindow

# Import the Plot
