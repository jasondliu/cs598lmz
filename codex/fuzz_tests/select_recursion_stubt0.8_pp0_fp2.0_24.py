import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    
    f = F()

    assert select.select([f], [], []) == ([f], [], [])
    assert select.select([f], [], []) == ([f], [], [])

def test_select_blocking():
    r, w = os.pipe()

    r = os.fdopen(r, "r", 0)
    w = os.fdopen(w, "w", 0)

    def target():
        time.sleep(0.1)
        w.write("hello")
        w.close()

    t = threading.Thread(target=target)
    t.start()

    rlist, wlist, xlist = select.select([r], [], [], 0)
    assert rlist == []

    t.join()

    rlist, wlist, xlist = select.select([r], [], [])
    assert rlist == [r]

    assert r.read() == "hello"
