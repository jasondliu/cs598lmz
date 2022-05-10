import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append('A')

    class G:
        def fileno(self):
            a.append('B')

    d = {}
    d[F()] = d[G()] = None

    for x in select.select([], d, [], 0)[1]:
        pass
    assert a == ['A', 'B']

    a.clear()
    for x in select.select([], d, [], 0)[1]:
        pass
    assert a == ['B']
