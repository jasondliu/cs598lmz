import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a)

# This example is from the _select.c module.  The code actually uses
# C code, but the Python module has the same problem.
#
# def test_select_closed_pipe():
#     import sys, os, signal
#     # Issue #11788: select() should not crash on a broken pipe
#     rfd, wfd = os.pipe()
#     os.write(wfd, b"x")
#     os.close(wfd)
#     for i in range(512):
#         try:
#             select.select([rfd], [], [], 0)
#         except OSError:
#             pass

test_select_mutated()
