import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    try:
        select.select([f], a, a)
    except RuntimeError:
        # we were lucky that the select() got called before the mutation
        # happened.
        pass

def test_select_closed_file():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    a.append(f)
    try:
        select.select([f], a, a)
    except ValueError:
        # we were lucky that the select() got called before the mutation
        # happened.
        pass

def test_select_closed_pipe():
    import os
    r, w = os.pipe()
    try:
        select.select([r], [r], [r])
    except ValueError:
        # we were lucky that the select() got called before the mutation
        # happened.
        pass
    finally:
        os.close(r)
        os.close(w)

