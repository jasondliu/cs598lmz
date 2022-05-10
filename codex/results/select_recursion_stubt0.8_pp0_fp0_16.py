import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())

    try:
        select.select([], [], a)
    except RecursionError:
        pass
    except ValueError:
        pass

def test_select_broken_pipe():
    # Set up a pipe with a read end that's been closed:
    r, w = os.pipe()
    os.close(r)
    # We don't expect this to throw but see issue #7169:
    select.select([], [w], [], 0)
    os.close(w)

def test_select_error_reading():
    # Set up a pipe with a read end that's been closed:
    r, w = os.pipe()
    os.close(r)
    # We don't expect this to throw but see issue #23819:
    select.select([w], [], [], 0)
    os.close(w)

class SelectableWrapper(object):
    """Wrapper that makes a file-like object selectable."""

    def __init__(self, fp):
        self
