import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    s = select.select([], [F()], [], 0.1)
    if s[1] or a:
        raise ValueError("FD not removed")

def test_poll_mutated():
    #  Test fix for http://bugs.python.org/issue19764

    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return a.pop()
    p = select.poll()
    p.register(F())
    p.poll()
    if a:
        raise ValueError("FD not removed")

@support.reap_threads
def test_main():
    th = threading.Thread(target=test_select_mutated)
    th.start()
    th.join()
    test_poll_mutated()

if __name__ == "__main__":
    test_main()
