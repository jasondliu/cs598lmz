import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
class db(threading.Thread):
    def __init__(self, file_name):
        threading.Thread.__init__(self)
        self.fn = file_name
        self.start()
    def run(self):
        self.cn = sqlite3.connect(self.fn)
        assert(self.cn.execute("create table x(x integer)") is None)
        assert(self.cn.execute("insert into x values (1)") is None)
        assert(self.cn.execute("insert into x values (2)") is None)
        self.cn.commit()
        assert(self.cn.execute("select count(*) from x").fetchone()[0] == 2)
        self.cn.close()
db("/tmp/lockhandler.sqlite")
# Get fd for the lock file
fd_fd = os.open("/tmp/lockhandler.sqlite-journal", os.O_RDWR)
# Get filename for the lock file
fd_fn = os.readlink("/proc/self/fd/%d
