import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 1)

def test_select_error():
    class F:
        def fileno(self):
            return -1

    select.select([F()], [], [], 1)

def test_error_conditions():
    # select.select()
    raises(TypeError, select.select, 1, 2, 3)
    raises(TypeError, select.select, [1], 2, 3)
    raises(TypeError, select.select, [], [2], 3)
    raises(TypeError, select.select, [], [], [3])
    raises(TypeError, select.select, "", "", "")
    raises(TypeError, select.select, [], [], [], "")

    # select.poll()
    raises(TypeError, select.poll)
    raises(TypeError, select.poll, 42)


class TestSelect:
    def test_select(self):
        r, w, x = select.select([], [], [], 0)
       
