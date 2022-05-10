import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    select.select(a, a, a, 10)

def test_select_error():
    a = [1]
    with raises(AttributeError):
        select.select(a, a, a, 10)

def test_select_many():
    a = []
    for i in range(select.PIPE_BUF + 1):
        if hasattr(os, 'pipe'):
            a.append(os.pipe())
        else:
            a.append('abc')
    select.select(a, a, a, 10)
