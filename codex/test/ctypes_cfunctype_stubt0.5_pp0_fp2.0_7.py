import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_py_object():
    e = Engine()
    e.load("""
    (declare-fun fun () PyObject)
    (assert (= (fun) 1))
    (check-sat)
    """)
    e.set("fun", fun)
    assert e.check() == sat

def test_py_object_array():
    e = Engine()
    e.load("""
    (declare-fun fun () (Array PyObject PyObject))
    (assert (= (fun 1) 1))
    (check-sat)
    """)
    e.set("fun", lambda i: i)
    assert e.check() == sat

def test_py_object_array_2():
    e = Engine()
    e.load("""
    (declare-fun fun () (Array PyObject PyObject))
    (assert (= (fun 1) 1))
    (assert (= (fun 2) 2))
    (check-sat)
    """)
    e.set("fun", lambda i: i)
    assert e.check
