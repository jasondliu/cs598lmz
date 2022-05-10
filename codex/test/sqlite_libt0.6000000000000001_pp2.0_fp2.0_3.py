import ctypes
import ctypes.util
import threading
import sqlite3
import os
from time import time, sleep

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Dictionary"
__version__ = "1.0"
__trigger__ = "dict "
__author__ = "Manuel Schneider"
__dependencies__ = []
__icon_path__ = "/usr/share/icons/hicolor/scalable/apps/org.gnome.Dictionary.svg"


def get_dictionary_path():
    for dictionary_path in ['/usr/share/dict/words']:
        if os.path.isfile(dictionary_path):
            return dictionary_path


class DictionaryExtension(Extension):

    def __init__(self):
        super(DictionaryExtension, self).__init__()
        self.subscribe("trigger", self.trigger)

    def trigger(self, _):
        dictionary_path = get_dictionary_path()
        if dictionary_path is None:
            return
