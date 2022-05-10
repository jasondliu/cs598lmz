import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Avoid TypeError: 'NoneType' object is not callable. See issue #3.
try:
  from PyQt4 import QtGui
  application = QtGui.QApplication(sys.argv)
except Exception:
  pass
