import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    a.append(F())
    select.select([], a, [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            # This will succeed with a select_mutated exception.
            test_select_mutated()
            return 42

    a.append(F())
    try:
        select.select([], [], a)
    except (select.error, ValueError):
        pass
    # Now we have replaced one of the lists.  The internal list of
    # file descriptors should b
