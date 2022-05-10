import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    f = F()
    a.append(f)

    try:
        select.select(a,a,a)
    except RuntimeError:
        pass

def test_select_timeout_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_timeout_mutated()

    f = F()
    a.append(f)

    try:
        select.select(a,a,a,1)
    except RuntimeError:
        pass


def test_select_error():
    a = []

    class F:
        def fileno(self):
            raise RuntimeError

    f = F()
    a.append(f)

    try:
        select.select(a,a,a)
    except RuntimeError:
        pass

def test_select_timeout_error():
    a = []

    class F:
        def fileno(self):
            raise RuntimeError

    f = F()
    a.append(f)

    try:
        select.select(a,a,a
