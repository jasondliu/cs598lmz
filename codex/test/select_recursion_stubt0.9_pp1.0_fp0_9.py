import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class G:
        def fileno(self):
            del a[:]
            return 0 # s.get() will crash due to mutation of the set

    def f():
        select.select([G()], [F()], [])

    a = [1]
    exc_raised = False
    try:
        f()
    except ValueError:
        exc_raised = True
    assert exc_raised, "ValueError should be raised when set is mutated."


def test_select_cannot_mutate_set():
    s = [select.kqueue()]
    s.pop()
    select.kqueue() # Executed to try to call ffi_close() on the popped kqueue


l = select.poll()
l.register(sys.__stdin__, select.POLLIN)
ready = l.poll()
# if stdin has data, then poll should return it
if ready[0][1] & select.POLLIN:
    sys.exit(0)
sys.exit(1)
