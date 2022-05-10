import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()])

def test_select_error():
    select.select([], [], [], 0)

def test_select_error2():
    select.select([], [], [], 0, 0)

def test_select_error3():
    select.select([], [], [], 0, 0, 0)

def test_select_error4():
    select.select([], [], [], 0, 0, 0, 0)

def test_select_error5():
    select.select([], [], [], 0, 0, 0, 0, 0)

def test_select_error6():
    select.select([], [], [], 0, 0, 0, 0, 0, 0)

def test_select_error7():
    select.select([], [], [], 0, 0, 0, 0, 0, 0, 0)
