import weakref

__all__ = ["QtCore", "QtGui", "QtWidgets", "Qt", "QtTest", "QtNetwork"]

QtCore, QtGui, QtWidgets, Qt, QtTest, QtNetwork = [None] * 6

def _import_qt(module):
    mod = __import__(module)
    components = module.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def _import_QtGui():
    import sip
    sip.setapi('QVariant', 2)
    sip.setapi('QString', 2)

    from PyQt5 import QtGui
    return QtGui


def _import_QtWidgets():
    import sip
    sip.setapi('QVariant', 2)
    sip.setapi('QString', 2)

    from PyQt5 import QtWidgets
    return QtWidgets


def _import_QtCore():
    import sip
    sip
