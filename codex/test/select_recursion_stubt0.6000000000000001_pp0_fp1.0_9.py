import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def read(self):
            return True

    a.append(F())
    a.append(F())

    while True:
        # This will always raise an exception on PyPy
        # because the length of the list changes
        # during the call to select.select()
        r, w, e = select.select(a, a, a, 0.1)
