import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a.append(F())
    a.append(F())

    for i in range(3):
        select.select(a, a, a)

def test_select_bogus_fd():
    bozo = []
    select.select([bozo], [bozo], [bozo], 0)

    bozo = {}
    bozo.__class__ = int
    select.select([bozo], [bozo], [bozo], 0)

    bozo = {}
    bozo.__class__ = float
    select.select([bozo], [bozo], [bozo], 0)

    bozo = ()
    select.select(bozo, bozo, bozo, 0)

def test_select_non_timeout():
    # The test_select tests have an implicit 0.001s timeout

    class Raiser:
        def fileno(self):
            return 1001
        def close(self):
            raise Exception

    orig_poll = select.poll
    try:
        select.poll = Raiser
       
