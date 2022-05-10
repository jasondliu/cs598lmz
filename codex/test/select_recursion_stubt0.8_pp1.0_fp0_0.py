import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def w():
        a.append(select.select([F()], [], []))

    newthread = thread.start_new_thread(w, ())
    time.sleep(1.0)
    # This used to crash:
    os.write(1, b'x')
    time.sleep(1.0)
    del a[:]

    a.append(select.select([F()], [], []))
    newthread = thread.start_new_thread(w, ())
    time.sleep(1.0)
    # This used to crash:
    os.write(1, b'x')
    time.sleep(1.0)

from test import support
support.run_unittest(__name__)
