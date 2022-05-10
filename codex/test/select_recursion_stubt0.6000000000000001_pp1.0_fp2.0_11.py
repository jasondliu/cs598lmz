import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    fd = select.select([], [], [], 0.1)


def test_timeout():
    import select
    # a timeout of 0.0 means "poll", which should return immediately
    select.select([], [], [], 0.0)


def test_select_keyboardinterrupt():
    import select
    raises(KeyboardInterrupt, select.select, [], [], [], -1)


def test_select_read_keyboardinterrupt():
    import select
    import os, errno
    # create a pipe, close one end
    r, w = os.pipe()
    os.close(w)
