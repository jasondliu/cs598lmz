import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def f(*args):
        a.append(3)
        a.append(4)
        return [F(), F()]

    prev = select.select
    try:
        select.select = f
        with pytest.raises(ValueError):
            fd = open('/etc/passwd', 'rb')
            try:
                select.select([fd], [], [])
            finally:
                fd.close()
    finally:
        select.select = prev
