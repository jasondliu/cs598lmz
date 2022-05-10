import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def run_test(test, name):
    try:
        test()
        print("%s: ok" % name)
    except:
        print("%s: failed" % name)
        raise

def test_pass():
    d = {'fun': fun}
    p = pickle.dumps(d)
    d2 = pickle.loads(p)
    assert d2['fun']() == 42

def test_pass2():
    d = {'fun': fun}
    p = pickle.dumps(d)
    d2 = pickle.loads(p)
    assert d2['fun']() == 42

def test_fail():
    d = {'fun': fun}
    p = pickle.dumps(d)
    d2 = pickle.loads(p)
    assert d2['fun']() == 42

def test_fail2():
    d = {'fun': fun}
    p = pickle.dumps(d)
    d2 = pickle.loads(p)
