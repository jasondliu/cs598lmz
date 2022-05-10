import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 123
    a.append(F())

    try:
        select.select([], a, a)
    except RuntimeError:
        pass

    b = "abc"
    try:
        select.select([], b, a)
    except TypeError:
        pass

    a.append(F())
    select.select([], a, a)

def test_bug_444727():
    # Bug #444727: AIX allows the select() timeout to be set to None.
    # It should be treated as a timeout of zero instead.
    cs,cw,ce = select.select([], [], [], None)
    assert cs == cw == ce == []

@pytest.mark.skipif('sys.platform != "win32" or sys.version_info >= (3,5)',
                    reason='windows and python version specific behaviour')
def test_win32_timeout_fraction():
    # Bug #5167
    if 'C:\Windows' not in sys.executable.upper():
        # This test only applies to a win32 build
