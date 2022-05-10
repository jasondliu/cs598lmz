import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [])
    assert not a

def test_select_mutated_after_error():
    class F:
        def fileno(self):
            return 1
        def close(self):
            test_select_mutated_after_error()

    try:
        select.select([F()], [], [])
    except select.error:
        pass

def test_select_mutated_after_error_FD():
    class F:
        def fileno(self):
            return 1
        def close(self):
            test_select_mutated_after_error_FD()
    import os
    try:
        select.select([F()], [], [], timeout=0, use_poll=False)
    except select.error:
        pass
    try:
        select.select([F()], [], [], timeout=0, use_poll=True)
    except select.error:
        pass
    #
    class F:
        def fileno(self):
           
