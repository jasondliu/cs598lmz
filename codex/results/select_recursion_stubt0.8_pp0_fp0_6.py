import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop(0)

    f = F()
    select.select([f], [f], [f], .1)

# The following test is expected to fail with errors about
# file descriptors when running with the default configuration.
# This is a known issue, see issue #4124

def test_select_mutated_raise_error():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_raise_error()
            return a.pop(0)

    f = F()
    try:
        select.select([f], [f], [f], .1)
    except (ValueError, IndexError):
        pass
    else:
        assert 0

# The following test is expected to fail with a fatal error
# when running with the default configuration.
# This is a known issue, see issue #4124

def test_select_mutated_raise_fatal():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_raise_fatal()
