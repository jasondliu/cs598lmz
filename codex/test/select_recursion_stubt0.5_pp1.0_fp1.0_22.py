import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    class G:
        def fileno(self):
            return 42

    class H:
        def fileno(self):
            return 42

        def close(self):
            a.append(43)

    select.select([F()], [G()], [H()], 0)

def test_select_interrupted():
    def fileno(self):
        return 42

    def close(self):
        raise KeyboardInterrupt

    class F:
        fileno = fileno
        close = close

    class G:
        fileno = fileno

    class H:
        fileno = fileno
        close = close

    try:
        select.select([F()], [G()], [H()], 0)
    except KeyboardInterrupt:
        pass

def test_select_error():
    def fileno(self):
        return 42

    def close(self):
        raise ValueError

    class F:
        fileno = fileno
        close = close

    class G:
        fileno = fileno

