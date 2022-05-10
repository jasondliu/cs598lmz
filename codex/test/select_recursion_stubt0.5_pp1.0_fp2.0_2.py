import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def __del__(self):
            a.append(1)

    select.select([F()], [], [])
    del a[:]
    select.select([F()], [], [])
    del a[:]
    select.select([F()], [], [])

def test_select_large_fd():
    # This test is known to fail on OS X 10.4, which has a hard-coded limit
    # of 1024 file descriptors.  We skip the test there.
    if sys.platform == 'darwin':
        from ctypes import cdll, c_int, byref
        libc = cdll.LoadLibrary('libc.dylib')
        open_max = c_int(0)
        libc.sysctlbyname('kern.num_files', byref(open_max),
                          ctypes.sizeof(open_max), None, 0)
        if open_max.value == 1024:
            return
    fds = []
