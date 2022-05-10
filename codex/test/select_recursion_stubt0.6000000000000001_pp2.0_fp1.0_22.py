import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(42)

    f = F()
    select.select([f], [], [])

def test_select_mutated_2():
    import select
    import subprocess
    import sys

    # See issue #19125.
    if sys.platform == 'win32':
        pytest.skip("Don't run this test on Windows")

    # Create a pipe, and set both ends to non-blocking.
    r, w = os.pipe()
    for fd in (r, w):
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    # Spawn a child that will write to the pipe.
