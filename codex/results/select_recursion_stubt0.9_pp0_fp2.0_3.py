import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    s = [F()]
    try:
        select.select(s, s, s)
        test_select_mutated()
    except ValueError:
        pass

def test_select_closed():
    for fd in (0,1,2):
        if os.isatty(fd): continue
        os.close(fd)

    try:
        select.select([], [], [])
    except ValueError:
        pass # "I/O operation on closed file" (python 2.5)
    except OSError:
        pass # "filedescriptor out of range in sys_select" (python 2.4)

    sys.stderr.write('\n')

def test_select_empty():
    assert select.select([], [], [], 0.0) == ([], [], [])

#def test_select_cycle():
#    try:
#        select.select([], [], [], -1)
#    except ValueError:
#        return


def test_select():
   
