import weakref
# Test weakref.ref.__call__()
TESTFUNC = lambda: None
w = weakref.ref(None)
def callback(reference):
    global test_obj, TESTFUNC
    test_obj(TESTFUNC)
w.__call__(callback)

""" <=== !  code  ! ===> """
