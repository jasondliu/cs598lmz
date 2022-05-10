import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def close(self):
            a.append(0)

    select.select([F()], [], [], 0)
    assert a == [0]

def test_select_keyboardinterrupt():
    import signal
    import os
    import select
    import sys

    if sys.platform == 'win32':
        pytest.skip("windows does not support signals")

    # The test is not reliable on OS/X Tiger:  it's possible that the
    # signal will be delivered before the select() call, which makes
    # the test fail.
    if sys.platform == 'darwin' and sys.version_info[:2] == (2, 3):
        try:
            darwin_version = int(os.uname()[2].split('.')[0])
        except ValueError:
            pass
        else:
            if darwin_version < 9:
                pytest.skip("test is not reliable on OS/X Tiger")

    signal.signal(signal.SIGALRM, lambda *args: None)
   
