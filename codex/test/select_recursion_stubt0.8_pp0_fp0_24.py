import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1
        def __del__(self):
            a.append(1)

    select.select([F()], [], [])

def test_str_str():
    assert type(str('abc')) is str

def test_str_bytearray():
    raises(TypeError, str, bytearray('abc'))

def test_u_overflow():
    raises(ValueError, unicode, 'xyz', 256)

def test_u_with_null():
    assert len(unicode('x\x00y')) == 2

def test_index_str():
    assert 'a'[0] == 'a'
    assert 'a'[-1] == 'a'
    raises(IndexError, lambda: 'a'[1])
    raises(IndexError, lambda: 'a'[-2])

def test_index_unicode():
    assert u'a'[0] == u'a'
    assert u'a'[-1] == u'a'
