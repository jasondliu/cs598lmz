import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [], 0)
    test_select_mutated()
    assert a == []

def test_get_poller_with_select():
    from gevent import select
    poller = select.get_poller()
    assert poller is select.select
