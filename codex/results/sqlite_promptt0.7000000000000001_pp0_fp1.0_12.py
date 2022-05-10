import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with a file in a directory that is removed.

libc = ctypes.CDLL(ctypes.util.find_library('c'))

def unlink(filename):
    libc.unlink(filename)

def rmdir(dirname):
    libc.rmdir(dirname)

def remove():
    # Remove a file.
    db = sqlite3.connect(':memory:')
    unlink(db.filename)
    db.close()

def remove_dir():
    # Remove a directory.
    dirname = '/tmp/sqlite3-test-dir-' + str(os.getpid())
    os.mkdir(dirname)
    db = sqlite3.connect(dirname + '/foo.db')
    rmdir(dirname)
    db.close()

t1 = threading.Thread(target=remove)
t2 = threading.Thread(target=remove_dir)
t1.start()
t2.start()
t1.join()
t2.join()
