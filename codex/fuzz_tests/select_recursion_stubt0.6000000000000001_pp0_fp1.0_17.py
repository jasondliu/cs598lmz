import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)

    # this used to crash because it would mutate the list of file objects
    # during the select, and then crash in the fileno() method.
    select.select([f], [], [])
