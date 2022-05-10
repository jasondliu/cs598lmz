import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 1)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return a.pop()

    select.select([F()], [], [], 1)

if sys.platform == "win32":
    def test_select_closed_fds():
        class F:
            def fileno(self):
                return -1
        select.select([F()], [], [], 1)

#def test_select_interrupted():
#    # This test is too unreliable to be useful.
#    class F:
#        def fileno(self):
#            raise KeyboardInterrupt
#    try:
#        select.select([], [], [], 1)
#    except KeyboardInterrupt:
#        pass
#    else:
#        assert 0, "KeyboardInterrupt not raised"

def test_select_bad_fd():
    class F:
        def
