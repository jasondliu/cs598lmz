import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([], [], [F()])
    assert a == []
    select.select([], [], [F()])
    assert a == [0]
    select.select([], [], [F()])
    assert a == [0, 1]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    select.select([], [], [F()])
    assert a == [1]
    select.select([], [], [F()])
    assert a == [1, 1]
    select.select([], [], [F()])
    assert a == [1, 1, 1]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    select.select([], [], [F()])
    assert a == [1]
    select.select
