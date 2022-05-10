import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 4

    select.select([F()], [], [])

    eq_(a, [1])

    class F2:
        def fileno(self):
            a.append(1)
            return 4


    select.select([F2()], [], [])

    eq_(a, [1, 1, 1])


class I:
    def fileno(self):
        return 4


class J:
    def fileno(self):
        return 4


class K:
    def fileno(self):
        return 5


class L:
    def fileno(self):
        return 6


def test_select_equal():
    a = []

    def fake_select(a, b, c, d):
        a.append((b, c, d))
        return [a], [b], [c]

    def fake_poll():
        return [a], [b], [c]

    def fake_epoll():
        return [a], [b], [c]

    fake_select.__
