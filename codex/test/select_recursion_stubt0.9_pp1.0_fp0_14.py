import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1
        def __del__(self):
            a.append(True)
            test_select_mutated()

    select.select([F()], [], [], 0)
    del a[:]
    select.select(["1"], [], [], 0)

    class F:
        __del__ = lambda self: a.extend(list("def"))

    select.select(["1"], [F()], [], 0)
    assert a == ["d", "e", "f"]

def test_select_fd_traceback():
    d = {}

    class File:
        def fileno(self): return 5
    class Module:
        File = File
        d = {}
    m = Module()
    d["Module"] = m

    def trace(frame, what, arg):
        if what == "call":
            if frame.f_code.co_name == "select":
                if d["Module"].d.get("delete"):
                    del d["Module"]
