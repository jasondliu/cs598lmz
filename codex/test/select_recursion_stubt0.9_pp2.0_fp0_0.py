import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()  # "recursing"
            return 5

    a.append(F())
    test_support.gc_collect()

    # a FD that is somewhere in the middle
    for i in range(4):
        s = os.open(".", 0)

    # the actual bug was hidden with try:finally:,
    # which resulted in the error in w_select() being ignored,
    # and the string being resurrected since the error prevented
    # _PyIO_FD_FREE()
    try:
        select.select([a[0]], [], [])
    finally:
        newvalue = 1

test_select_mutated()


def test_select_closed():
    # You must call FD_CLR(0, &fdset) first, and you need to call it before
    # FD_ISSET(0, &fdset) can return 0
    r, w, x = select.select([0], [], [], 0)
