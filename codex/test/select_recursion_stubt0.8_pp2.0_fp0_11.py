import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    s = select.select([], [F()], [], 0)
    s[1][0].fileno()

class A:
    def fileno(self):
        return 4

class B(A):
    def fileno(self):
        return 5

def test_select_precious():
    a = []
    a.append(A())
    a.append(B())
    s = select.select([], a, [], 5)
    assert 3 == len(s[1])

def test_select_on_list():
    a = []
    a.append(1)
    select.select([a], a, a, 5)
    a.append(2)

def test_select_timeout():
    for i in range(5):
        select.select([], [], [], 0.1)

class C:
    pass

def test_select_on_object():
    c = C()
