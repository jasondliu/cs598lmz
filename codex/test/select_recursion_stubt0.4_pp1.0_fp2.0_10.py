import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    try:
        select.select([], [F()], [])
    except ValueError:
        pass
    else:
        raise RuntimeError("didn't raise ValueError")

    # XXX This is a hack.  The actual bug is that select() mutates the
    # XXX list it's given, and this is a test for that.  But we can't
    # XXX check that directly, because it's legal for select() to
    # XXX modify the list.  The real bug is that, if the list is
    # XXX modified, the select() loop in Modules/selectmodule.c doesn't
    # XXX notice and keeps looping forever.  This test tries to tickle
    # XXX that bug, but there's a race condition: if the list modification
    # XXX happens after the select() loop in Modules/selectmodule.c has
    # XXX already noticed that the list is empty, this test passes
    # XXX spuriously.  I haven't been able to figure out how to get rid
    # XXX of that race condition.
