import weakref
import sys
import functools

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from . import config
from . import icons
from . import util
from . import widgets
from . import data


class QStandardItemModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)
        self.__items = {}
        self.__indexes = {}
        self.__key_func = None

    def setKeyFunc(self, func):
        self.__key_func = func

    def keyFunc(self):
        return self.__key_func

    def setItem(self, key, item):
        if self.__key_func is not None:
            key = self.__key_func(key)
        self.__items[key] = item
        self.__indexes[key] = self.indexFromItem(item)

    def item
