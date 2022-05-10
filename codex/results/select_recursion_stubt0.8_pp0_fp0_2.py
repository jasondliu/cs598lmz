import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    def do_select():
        a.append(1)
        select.select([F()], [], [])
        a.append(2)

    do_select()
    do_select()
    a == [1,2]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            a.append(42)

    def do_select():
        a.append(1)
        select.select([F()], [], [])
        a.append(2)

    do_select()
    do_select()
    a == [1,42,2]
