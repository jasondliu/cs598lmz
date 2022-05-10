import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    exc = None
    try:
        select.select([], [F()], [])
    except ValueError as e:
        exc = e

    assert exc is not None


def test_all_and_any():
    def throws(exc):
        raise exc

    all_exc = None
    any_exc = None
    try:
        all(throws(KeyboardInterrupt) for x in ())
    except KeyboardInterrupt as e:
        all_exc = e

    try:
        any(throws(KeyboardInterrupt) for x in ())
    except KeyboardInterrupt as e:
        any_exc = e

    assert all_exc is not None
    assert any_exc is not None


def test_bytearray_hash():
    class C(object):
        hash = None
        def __hash__(self):
            if self.hash is None:
                return object.__hash__(self)
            return self.hash
        __eq__ = object.__eq__

    o = C()
    o.hash = 0xFFFFFFFF

