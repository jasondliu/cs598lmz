import ctypes
import ctypes.util
import threading
import sqlite3
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import (
    QObject,
    pyqtSlot,
)


class Clipboard(QObject):

    def __init__(self):
        super().__init__()
        self.cb = gtk.Clipboard()
        thread = threading.Thread(target=self.monitor_clipboard)
        thread.start()
    
    def get_text(self):
        return self.cb.wait_for_text()
        
    def monitor_clipboard(self):
        self.cb.set_text('test')
        self.cb.wait_for_text()
        while True:
            time.sleep(2)
            if self.cb.wait_is_text_available():
                self.cb.request_text(self.cb_changed)
    
    def cb_changed(text):
        # print('clipboard changed')
        # print(text)
        pass


class SQLiteDB():

    def __init__(self, filename):

