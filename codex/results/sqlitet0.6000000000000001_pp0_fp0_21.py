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

libtest_sqlite3_so = ctypes.util.find_library("test_sqlite3")
libtest_sqlite3 = ctypes.CDLL(libtest_sqlite3_so)

libtest_sqlite3.test_sqlite3(my_cb)
</code>
libtest_sqlite3.c
<code>#include &lt;Python.h&gt;
#include &lt;sqlite3.h&gt;

#define DECLARE_SQLITE3_CALLBACK(name) \
    static int name(void *p)

DECLARE_SQLITE3_CALLBACK(my_cb);

static int
my_cb(void *p)
{
    PyObject *arglist = Py_BuildValue("(O)", p);
    PyObject *result = PyEval_CallObject(cb, arglist);
    Py_DECREF(arglist);
    return PyLong_AsLong(result);
}

static PyObject *
test_sqlite3(PyObject *self, PyObject *args)
