import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_exc():
    a = []

    class F:
        def fileno(self):
            raise Exception(str(len(a)))

    F().fileno()
    try:
        select.select([F()], [], [])
        assert False, "DID NOT RAISE"
    except Exception as e:
       assert e.args[0] == "0"

def test_select_exc2(): # coverage
    a = []

    class F:
        def fileno(self):
            raise Exception(str(len(a)))

    F().fileno()
    try:
        select.select([], [F()], [])
        assert False, "DID NOT RAISE"
    except Exception as e:
        assert e.args[0] == "0"

def test_select_exc3(): # coverage
    a = []

    class F:
        def fileno(self):
            raise Exception(str(len(a)))

    F
