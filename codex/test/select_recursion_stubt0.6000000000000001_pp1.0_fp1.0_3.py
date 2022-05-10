import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def close(self):
            a.append(0)

    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

# test that select() doesn't modify the passed-in lists and dicts
def test_select_in():
    read_in = [object()]
    write_in = [object()]
    except_in = [object()]
    timeout = object()
    select.select(read_in, write_in, except_in, timeout)
    assert read_in == [object()]
    assert write_in == [object()]
    assert except_in == [object()]
    assert timeout is object()

# test that select() raises ValueError if any of the passed-in objects
# are not file descriptors.
def test_select_bad_fd():
    class NotAFileDescriptor:
        pass
