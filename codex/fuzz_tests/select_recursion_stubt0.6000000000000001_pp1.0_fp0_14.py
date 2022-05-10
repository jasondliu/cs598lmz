import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0.0)
    assert a == []

def test_select_keyboardinterrupt():
    import time
    import os
    from threading import Thread

    def target():
        time.sleep(0.1)
        os.kill(os.getpid(), signal.SIGINT)

    thr = Thread(target=target)
    thr.start()
    try:
        select.select([], [], [], 1.0)
    except KeyboardInterrupt:
        pass
    else:
        assert False

def test_select_keyboardinterrupt_not_raised():
    from threading import Thread

    def target():
        select.select([], [], [], 1.0)

    thr = Thread(target=target)
    thr.start()
    # wait for thread to start
    time.sleep(0.1)
    os.kill(os.getpid(), signal.SIGINT)
    thr.join()

def test_select_keyboardinterrupt_interrupted():
   
