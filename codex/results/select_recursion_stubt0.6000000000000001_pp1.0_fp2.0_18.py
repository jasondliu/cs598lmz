import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()], 10)

def test_select_closed_file_object():
    class F:
        def fileno(self):
            return 1

        def close(self):
            pass

    f = F()
    f.fileno()
    f.close()
    f.fileno()

def test_select_bad_file_object():
    class F:
        def fileno(self):
            return "hello"

    select.select([F()], [F()], [F()], 10)

def test_select_closed_pipe():
    r, w = os.pipe()
    fd = os.dup(r)
    os.close(r)
    os.close(w)
    try:
        select.select([fd], [], [], 0)
    except:
        pass
    try:
        select.select([fd], [], [], 0)
    except:
        pass

def test_select_bad_pipe():
   
