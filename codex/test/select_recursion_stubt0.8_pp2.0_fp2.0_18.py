import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # infinite loop
            return a.pop()

    a.append(F())
    select.select([F()], [F()], [F()], 5)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(F()) # infinite loop, but only after some time
            return a.pop()

    a.append(F())
    select.select([F()], [F()], [F()], 5)

def test_poll_mutated():
    class F:
        def fileno(self):
            return test_poll_mutated() # infinite loop
    p = select.poll()
    p.register(F(), select.POLLIN)
    p.poll(5)

def test_poll_mutated2():
    class F:
        def fileno(self):
            return a[-1] # infinite loop, but only after some time
    a = [F()]
    p = select.poll()
