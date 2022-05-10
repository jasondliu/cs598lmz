import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PySide import QtCore, QtGui

from . import qtutils


def open_file(parent, title):
    """Wrapper for getting a filename from the user"""
    return qtutils.open_file(parent, title)


def open_files(parent, title):
    """Wrapper for getting a filename from the user"""
    return qtutils.open_files(parent, title)


def save_file(parent, title):
    """Wrapper for getting a filename from the user"""
    return qtutils.save_file(parent, title)


def directory(parent, title):
    """Wrapper for getting a directory from the user"""
    return qtutils.directory(parent, title)


def information(parent, msg, title='', informative_text='',
                detailed_text=''):
    """Show a modal information dialog"""
    return qtutils.information(parent, title, msg, informative_text, detailed_text)


