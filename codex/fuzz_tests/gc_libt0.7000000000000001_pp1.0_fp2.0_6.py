import gc, weakref

from PyQt5.QtCore import (QObject, QVariant, pyqtSignal, pyqtProperty,
                          QMetaObject, QMetaMethod, Q_ARG, Q_RETURN_ARG)
from PyQt5.QtQml import QJSValue


def _QVariant_to_python(variant):
    """
    Convert a QVariant to a Python object.
    """
    if not isinstance(variant, QVariant):
        return variant

    t = variant.type()
    if t == QVariant.Invalid:
        return None
    elif t == QVariant.Bool:
        return variant.toBool()
    elif t == QVariant.Char:
        return variant.toChar()
    elif t == QVariant.String:
        return variant.toString()
    elif t == QVariant.Int:
        return variant.toInt()[0]
    elif t == QVariant.UInt:
        return variant.toUInt()[0]
    el
