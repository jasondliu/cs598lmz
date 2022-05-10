import weakref

from PyQt5.QtCore import (
    QAbstractItemModel,
    QModelIndex,
    Qt,
    pyqtSignal,
    pyqtSlot,
)

from . import _core
from . import _view


class QmlObject(object):
    """Base class for all QML objects.

    This is a mixin class and should not be used directly.
    """

    _qml_object = None
    _qml_context = None
    _qml_attached_properties = {}
    _qml_attached_properties_changed = {}

    def __init__(self):
        self._qml_attached_properties = {}
        self._qml_attached_properties_changed = {}

    def __del__(self):
        if self._qml_object is not None:
            self._qml_object.destroy()

    def __getattr__(self, name):
        if name.startswith("_qml_"):
            raise AttributeError(name)
        if self._qml_object
