import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    def remove_f():
        a.append(2)
        s.remove(f)

    s = select.select([], [f], [])
    f = F()
    remove_f()
    s = select.select([], [f], [])
    remove_f()
    assert a == [2,2]

def test_select_error():
    s = select.select([], [], [], 1)
    import threading
    x = threading.Event()
    def f():
        x.wait()
    t = threading.Thread(target=f)
    t.start()
    raises(ValueError, select.select, [], [], [], 1, None)
    x.set()
    t.join()

def test_select_poll_error():
    import _minimal_c_select
    s = select.poll()
    raises(ValueError, s.poll, 1, None)

def test_select_poll_mutated():
    a = []

    class F:

