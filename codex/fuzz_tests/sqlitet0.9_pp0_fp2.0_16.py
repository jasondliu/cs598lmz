import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

assert ctypes.util.find_library("sqlite3")
sqlite3.sqlite_version_info

sqlite3.enable_callback_tracebacks(True)
sqlite3.sqlite_open_v2(":memory:", 0, "": ctypes.c_char_p):

db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
if str(threading.current_thread()) == "MainThread":
    db.set_progress_handler(my_cb, 5)

db.executescript("""
pragma busy_timeout = 50;

create table foo (id integer primary key, name text (32));
create table bar (id integer primary key, name text (32));

insert into foo (name) values ('connie');
insert into foo (name) values ('macgod');
insert into foo (name) values ('n8');
insert into foo (name) values ('thumper');
insert into foo (name) values ('nemo');
insert into foo (name) values ('jep');

