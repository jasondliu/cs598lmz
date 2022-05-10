import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 0

        def do_not_call(self):
            # Calling this method with the result of the test causes
            # the test to leave a reference to itself in a cycle,
            # making it impossible to clear the test from memory before
            # calling resource.getrusage().
            pass

    f = F()
    r = select.select([f], [], [], 0.1)
