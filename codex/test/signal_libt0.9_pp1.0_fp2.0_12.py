import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtNetwork import QNetworkProxy, QNetworkRequest, QAbstractNetworkCache, QNetworkAccessManager
from epubcreator.creator import EpubCreator, DEFAULT_PAGE
from epubcreator.creator import LANGUAGE_MAP as LANG_MAP


def _empty(p):
    pass

def get_family_switch(family):
    if family == 'serif':
        return True
    if family == 'sans-serif':
        return False
    if family.lower() in ['times', 'times new roman']:
        return True
    if family.lower() in ['helvetica', 'arial']:
        return False
    return True

def get_text_color(color):
    color = color.name().strip()
    if color.startswith('#'):
        color = color[1:]
