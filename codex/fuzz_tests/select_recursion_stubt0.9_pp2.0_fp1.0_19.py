import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 623

    select.select([F(), a], [], [])

    raise Exception

def test_selecta():
    select.select([], [], [], 5.21)


def test_selectb():
    select.select([], [], [], 3.2)


def test_selectc():
    select.select([], [], [], 'aim')


def test_selectd():
    select.select('python', object(), object(), object())


def test_selecte():
    select.select([], [], [], 0.125)

def test_selectf():
    select.select([], [], [], 5.21)


def test_selectg():
    import _io
    select.select([_io.FileIO('/dev/zero', 'r'), _io.FileIO('/dev/zero', 'r')], [], [], 5.21)

def test_selecth():
    import _io
    select.select([_io.FileIO('/dev/zero', 'r')], [], [], 5.
