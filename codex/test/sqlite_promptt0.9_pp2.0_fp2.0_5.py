import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

import gettext
import locale
from   modules.myConstants import Messages as Messages

class GenThread(threading.Thread):
    '''Common thread for all the pyBOMBS recipes.'''

    def __init__(self, queue, genSqlDict, log, runLock):
        threading.Thread.__init__(self)
        self.queue     = queue
        self.conn      = None
        self.genSqlDict   = genSqlDict
        self.genSqlDictLock = threading.Lock()
        self.log       = log
        self.runLock   = runLock

    def run(self):
        '''Run the thread for pyBOMBS recipes.'''
        self.log.info('genThread {} started'.format(threading.current_thread()))
        try:
            conn = sqlite3.connect('tmp' + threading.get_ident().__str__() + '.db')
            conn.executescript(Messages.sqlCreate)
            conn.commit()
        except Exception as inst:
            self
