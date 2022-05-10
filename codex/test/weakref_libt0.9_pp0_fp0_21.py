import weakref

from taurus import ExternalApp, TaurusException
from taurus.external.qt import Qt


def loadUi(filename, prefix = None):
    """Convenience function that loads a ui form and returns an instance of it
    wrapped inside a QWidget.

    :param filename: (str) the file name of the ui file.
                Currently only the filenames ending in ".ui" are supported
    :param prefix: (str) the prefix to be used to qualify the UI classes.
                It is mostly used internally by taurus to avoid name clashes.
    :return: (QWidget or subclass)"""
    return loadWidget(filename, prefix)


