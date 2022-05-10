import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 0

    [f for f in select.select([F()], [], [], 1)[0]]


@support.impl_detail("the posix module is too low-level to be mocked")
@pytest.mark.skipif(not hasattr(select, 'kqueue'), reason = "couldn't import kqueue")
class TestKqueueFallbackSelect:
    def setup_class(cls):
        if select.kqueue is NotImplemented:
            pytest.skip('kqueue is not implemented on this platform')

    def test_kqueue(self):
        import _testcapi
        kqueue = _testcapi.get_test_kqueue() # should raise if not implemented
        e1 = select.kevent(1, select.KQ_FILTER_READ, select.KQ_EV_ADD |
                           select.KQ_EV_ENABLE | select.KQ_EV_ONESHOT,
                           flags = select.KQ_NOTE_EXTEND)
