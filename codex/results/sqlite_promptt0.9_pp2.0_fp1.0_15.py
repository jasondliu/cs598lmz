import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') support

class ThreadedTempFile(threading.Thread):
    def __init__(self):
        super(ThreadedTempFile, self).__init__()
        self.fh = None
    def run(self):
        f, self.name = tempfile.mkstemp()
        self.fh = os.fdopen(f, 'wb')
        self.fh.close()
        self.fh = None

def test_open_tempfile(th=None):
    if th is None:
        th = ThreadedTempFile()
    th.start()
    th.join()
    try:
        conn = sqlite3.connect(':memory:')
        conn.execute('create table temp(foo)')
        conn.execute('insert into temp values ("hello world")')
        actual = conn.execute('select foo from temp').fetchall()
        this(actual, [('hello world',)])
    finally:
        try:
            os.unlink(th.name)
        except Exception as e:
            print(
