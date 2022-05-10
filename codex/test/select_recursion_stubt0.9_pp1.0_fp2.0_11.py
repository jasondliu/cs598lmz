import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def do_not_call(self):
            pass

    select.select([F()], [], [])

def test_unhandled_exception():
    prev_handler = PyOS_InputHook()
    try:
        # this raises an unhandled exception
        foo()
    finally:
        PyOS_InputHook()
    assert prev_handler == PyOS_InputHook()

def test_interrupting_threaded_application():
    import _thread
    import time

    def f():
        time.sleep(1)

    _thread.start_new_thread(f, ())
    time.sleep(0.1)
    PyOS_InputHook()


def test_update_after_ctrl_c():
    import threading
    import time

    def f():
        time.sleep(2)

    t = threading.Thread(target=f)
    t.start()
    time.sleep(0.1)
    try:
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        pass
