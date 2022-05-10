import weakref
# Test weakref.ref:

class Dummy:
    pass

dummy = Dummy()
dummy.foo = 'bar'

def check_ref_status(wr, expected_status):
    try:
        wr()
    except ReferenceError:
        assert expected_status == "dead"
    else:
        assert expected_status == "alive"


def test_ref_basic():
    wr = weakref.ref(dummy)
    check_ref_status(wr, "alive")
    del dummy
    check_ref_status(wr, "dead")
    dummy = Dummy()
    check_ref_status(wr, "dead")
    dummy.foo = 'bar'
    wr = weakref.ref(dummy)
    check_ref_status(wr, "alive")
    del dummy
    check_ref_status(wr, "dead")


def test_ref_leak():
    dummies = []
    for i in range(3000):
        dummy = Dummy()
        dummy.foo = 'bar'
        wr = weakref.ref(
