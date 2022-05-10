import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    try:
        select.select(a, a, a)
    except ValueError as e:
        pass
    else:
        raise Exception("Expected ValueError")

try:
    select.select([], [], [], timedelta(seconds=1))
except TypeError:
    pass
else:
    raise Exception("timedelta() unexpectedly allowed")
