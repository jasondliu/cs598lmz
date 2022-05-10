import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    assert select.select([F()], [], [], 0) == ([], [], [])

def test_select_keyboard_interrupt():
    raises(KeyboardInterrupt, select.select, [], [], [], 0)

def test_select_bad_list():
    class BadList(list):
        def __iter__(self):
            return self
        def __next__(self):
            raise StopIteration
    raises(TypeError, select.select, BadList(), [], [], 0)

def test_select_bad_fd():
    class BadFD:
        def fileno(self):
            return 'spam'
    raises(TypeError, select.select, [BadFD()], [], [], 0)

def test_select_bad_timeout():
    raises(TypeError, select.select, [], [], [], "spam")
