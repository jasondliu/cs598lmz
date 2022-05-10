import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 4

    f = F()
    select.select((f,), (), ())
    assert a == [1]

def test_select_error_in_method():
    class F:
        def fileno(self):
            raise ValueError
    select.select((F(),), (), ())

def test_select_bad_file_descriptor():
    try:
        select.select([2], [], [])
    except select.error as e:
        assert e.args[0] == errno.EBADF

def test_select_bad_file_descriptor_interp_level():
    class F:
        def fileno(self):
            return 2
    try:
        select.select([F()], [], [])
    except select.error as e:
        assert e.args[0] == errno.EBADF

