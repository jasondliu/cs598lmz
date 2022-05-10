import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().  For a more benign test, see test_weakref.py.

def check_cnt(cnt=5, cnt_max=10):
    if cnt < cnt_max:
        import time
        time.sleep(0.01)
        return check_cnt(cnt+1, cnt_max)

check_cnt() # wait till the system is calm

def bug(x):
    x = 0
    gc.collect()
    del x
    gc.collect()
    gc.collect()

def test(x):
    gc.collect()
    del x
    gc.collect()
    gc.collect()

bug(2)
test(2)

bugs = []
bugs.append(bugs)
del bugs
gc.collect()
gc.collect()

# Test iterating over the stack to find circularities.

class G1:
    def __init__(self):
        self.next = None

class G2:
    def __init__(self):
        self.next =
