import weakref

from PyQt5.QtCore import QObject, QEvent, pyqtSignal, QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QKeySequence
from PyQt5.QtWidgets import QShortcut, QWidget


class MyQShortcut(QShortcut):
    def __init__(self, parent, shortcut, handler):
        super().__init__(QKeySequence(shortcut), parent)
        self.activated.connect(lambda: handler(self))


class MyQObject(QObject):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent)
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        return getattr(self.parent(), item)


class EventFilter(QObject):
    def __init__(self, parent, types):
        super().__init__(parent)
        self.parent = weakref.ref(parent)
