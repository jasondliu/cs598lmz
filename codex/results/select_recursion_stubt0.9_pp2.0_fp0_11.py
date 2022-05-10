import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 6
        def read(self):
            a.append(6)
            return 'foo'

    b = []
    select.select([F()], [], [])
    assert b == []
    assert a == []
    x = sys.modules['select']
    try:
        del sys.modules['select']
        open('/dev/null', 'r+')
    finally:
        sys.modules['select'] = x
        x.select([F()], [], [])

def test_os_getenv_empty_string():
    from os import posixpath
    assert posixpath.getenv('FOO') == None

def test_prebuilt_cannot_go():
    py.test.skip("CPython 2.6 uses Distutils, which doesn't work on pypy")
    py.test.raises(OError, "os.listdir('/')")

def test_tempdir():
    import py
    tmpdir = py.test.ensuretemp("test_os")
    tmpdir.chdir()
    assert
