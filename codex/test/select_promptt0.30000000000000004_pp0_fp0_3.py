import select
# Test select.select()

def test_select():
    r, w, x = select.select([], [], [], 0.0)
    assert r == w == x == [], "select() returned non-empty lists"

def test_select_timeout():
    import time
    start = time.time()
    r, w, x = select.select([], [], [], 0.1)
    end = time.time()
    assert end - start >= 0.1, "timeout not respected"
    assert r == w == x == [], "select() returned non-empty lists"

def test_select_keyboardinterrupt():
    import time
    import threading
    import sys
    import os

    # We need to use a thread here to be able to interrupt the select() call
    # with a signal
    def target():
        time.sleep(0.1)
        os.kill(os.getpid(), signal.SIGINT)

    t = threading.Thread(target=target)
    t.start()
