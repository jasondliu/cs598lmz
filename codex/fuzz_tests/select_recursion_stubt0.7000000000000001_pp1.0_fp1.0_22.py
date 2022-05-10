import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

        def read(self):
            a.append(1)

    class G:
        def read(self):
            a.append(2)

    select.select([F()], [], [])
    select.select([G()], [], [])
    assert a == [1, 2], a

def test_select_str_and_bytes():
    # Issue #20934
    select.select([b'foo', 'bar'], [], [])
    select.select(['foo', b'bar'], [], [])
    with raises(TypeError):
        select.select(['foo', 'bar'], [], [5])
    with raises(TypeError):
        select.select([b'foo', b'bar'], [], [5])

def test_select_options():
    # Issue #20384
    select.select([], [], [], None)
