import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # this should not crash
            a.append(1)
            return 42
    f = F()
    test_thread_state.add_cleanup(test_select_mutated, f)

    # Force the select code to be recognized as _PySelect_Select -
    # this is not a complete test of select.select().
    try:
        select.select(a, a, a, -1)
    except ValueError:
        pass

    a = []
    # This should not crash
    select.select([f], [], [])
    assert a != []

def test_select_proxy_fds():
    import sys
    import os
    from rpython.translator.tool.cbuild import ExternalCompilationInfo
    from rpython.rlib.rarithmetic import intmask
