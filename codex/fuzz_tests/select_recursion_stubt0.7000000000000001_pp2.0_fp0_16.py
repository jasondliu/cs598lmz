import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    s = select.select([F()], [], [], 0)

def test_select_keyboardinterrupt():
    # Issue #7995: select() must not be interrupted by a signal
    # (ex.: a SIGINT); if it is, select() is retried.
    class InterruptedSelect(Exception):
        pass

    class KeyboardInterruptFail(Exception):
        pass

    def fail_select(*args):
        raise KeyboardInterruptFail()

    def interrupted_select(*args):
        raise InterruptedSelect()

    def check_interrupted_select(*args):
        try:
            select.select(*args)
        except InterruptedSelect:
            pass
        else:
            raise AssertionError("interrupted select() did not retry")

    saved_select = select.select
    try:
        select.select = fail_select
        try:
            select.select([], [], [], 0)
        except KeyboardInterrupt:
            pass
        else:
            raise AssertionError("select() did not raise "
                                 "
