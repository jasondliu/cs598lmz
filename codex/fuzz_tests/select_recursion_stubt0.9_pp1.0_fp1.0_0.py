import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())

    try:
        select.select([], [], [], 1)
    except Exception as e:
        # CPython raises RuntimeError, while PyPy raises a plain ValueError
        pass
    else:
        assert False
    del a[:]

    import gc
    gc.collect()

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())

    try:
        select.select([a], [], [], 1)
    except Exception as e:
        pass
    else:
        assert False

# tests select.source_tracking
class FileLike(object):
    def __init__(self):
        lltype.malloc(struct.file_desc, flavor='raw', track_allocation=True)
        self.fd = lltype.malloc(struct.file_desc, flavor='raw')

    def fileno(self):
        return int(self.fd)

def test_select_source_tracking():
    f0 = FileLike()
    f
