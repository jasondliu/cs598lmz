import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # recurse!
            a.append(self)
            return len(a)
    f = F()

    assert select.select([f], [f], [f], 0) == ([f], [f], [f])


def test_select_keyboardinterrupt():
    def interrupt():
        raise KeyboardInterrupt
    p = multiprocessing.Process(target=interrupt)
    p.start()

    assert select.select([], [], [], 0) == ([], [], [])
    p.join()


def test_select_keyboardinterrupt_2():
    def interrupt():
        raise KeyboardInterrupt
    p = multiprocessing.Process(target=interrupt)
    p.start()

    assert select.select([p], [], [], 0) == ([], [], [])
    p.join()


def test_select_keyboardinterrupt_3():
    def interrupt():
        raise KeyboardInterrupt
    p = multiprocessing.Process(target=interrupt)
    p.start()

