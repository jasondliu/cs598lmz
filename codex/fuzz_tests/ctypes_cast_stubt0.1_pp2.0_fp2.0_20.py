import ctypes
ctypes.cast(0, ctypes.py_object)

# imports for Python2
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

# import for PyQt5
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
except ImportError:
    raise ImportError("PyQt5 required")

# import for PyQt4
try:
    import PyQt4.QtCore as QtCore
    import PyQt4.QtGui as QtGui
    from PyQt4.QtCore import QObject, pyqtSlot, pyqtSignal
except ImportError:
    raise ImportError("PyQt4 required")

# import for PySide (untested)
try:
    import PySide.QtCore as QtCore
    import PySide.QtGui as QtGui
    from PySide.QtCore import QObject, Slot, Signal
except ImportError:
